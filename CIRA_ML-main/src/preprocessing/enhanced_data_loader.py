# src/preprocessing/enhanced_data_loader.py
"""
Enhanced Data Loader supporting multiple datasets for CIRA-ML
Supports UNSW-NB15, IoT-23, and custom datasets
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os
from typing import Tuple, Optional, Dict, Any

class EnhancedDataLoader:
    """Enhanced data loader supporting multiple IoT/IIoT datasets"""

    def __init__(self):
        self.data = None
        self.scaler = StandardScaler()
        self.encoders = {}
        self.dataset_name = None
        self.feature_names = []

        # Dataset-specific configurations
        self.dataset_configs = {
            'UNSW-NB15': {
                'files': ['UNSW_NB15_training-set.csv', 'UNSW_NB15_testing-set.csv'],
                'attack_col': 'attack_cat',
                'label_col': 'label',
                'risk_mapping': {
                    'Normal': 'Low',
                    'Generic': 'Medium',
                    'Exploits': 'High',
                    'Fuzzers': 'Medium',
                    'DoS': 'High',
                    'Reconnaissance': 'Medium',
                    'Analysis': 'Medium',
                    'Backdoor': 'High',
                    'Shellcode': 'High',
                    'Worms': 'High'
                },
                'exclude_cols': ['id', 'label', 'attack_cat', 'risk_level']
            },
            'IoT-23': {
                'files': ['IoT-23.csv'],  # Simulated
                'attack_col': 'label',
                'label_col': 'detailed-label',
                'risk_mapping': {
                    'Benign': 'Low',
                    'Malware': 'High',
                    'C&C': 'High',
                    'DDoS': 'High',
                    'Okiru': 'High',
                    'FileDownload': 'Medium',
                    'HeartBeat': 'Low',
                    'Torii': 'High',
                    'Mirai': 'High',
                    'PartOfAHorizontalPortScan': 'Medium'
                },
                'exclude_cols': ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'label', 'detailed-label', 'risk_level']
            },
            'Custom': {
                'files': ['custom_dataset.csv'],
                'attack_col': 'attack_type',
                'label_col': 'label',
                'risk_mapping': {
                    'normal': 'Low',
                    'attack': 'High'
                },
                'exclude_cols': ['label', 'attack_type', 'risk_level']
            }
        }

        # Available datasets
        self.available_datasets = list(self.dataset_configs.keys())

    def get_available_datasets(self) -> list:
        """Get list of supported datasets"""
        return self.available_datasets

    def simulate_iot23_data(self, n_samples: int = 100000) -> pd.DataFrame:
        """Simulate IoT-23 dataset structure for demonstration"""
        np.random.seed(42)

        # IoT-23 typical features (simplified)
        data = {
            'ts': pd.date_range('2023-01-01', periods=n_samples, freq='1s'),
            'uid': [f'C{i:06d}' for i in range(n_samples)],
            'id.orig_h': [f'192.168.1.{np.random.randint(1, 255)}' for _ in range(n_samples)],
            'id.orig_p': np.random.randint(1024, 65535, n_samples),
            'id.resp_h': [f'10.0.{np.random.randint(0, 255)}.{np.random.randint(1, 255)}' for _ in range(n_samples)],
            'id.resp_p': np.random.choice([80, 443, 22, 21, 25, 53, 8080], n_samples),
            'proto': np.random.choice(['tcp', 'udp', 'icmp'], n_samples, p=[0.7, 0.25, 0.05]),
            'service': np.random.choice(['http', 'https', 'ssh', 'dns', 'smtp', 'unknown'], n_samples),
            'duration': np.abs(np.random.normal(10, 5, n_samples)),
            'orig_bytes': np.abs(np.random.exponential(1000, n_samples)),
            'resp_bytes': np.abs(np.random.exponential(500, n_samples)),
            'conn_state': np.random.choice(['SF', 'S0', 'REJ', 'RSTO'], n_samples),
            'local_orig': np.random.choice([True, False], n_samples),
            'local_resp': np.random.choice([True, False], n_samples),
            'missed_bytes': np.random.poisson(0.1, n_samples),
            'history': np.random.choice(['Dd', 'Ad', 'Sh', 'h'], n_samples),
            'orig_pkts': np.abs(np.random.poisson(10, n_samples)),
            'orig_ip_bytes': np.abs(np.random.exponential(1200, n_samples)),
            'resp_pkts': np.abs(np.random.poisson(8, n_samples)),
            'resp_ip_bytes': np.abs(np.random.exponential(800, n_samples)),
            'tunnel_parents': ['(empty)'] * n_samples,
        }

        # Create labels (80% benign, 20% malicious)
        labels = np.random.choice(['Benign', 'Malware'], n_samples, p=[0.8, 0.2])
        detailed_labels = []

        for label in labels:
            if label == 'Benign':
                detailed_labels.append('Benign')
            else:
                detailed_labels.append(np.random.choice([
                    'Mirai', 'Torii', 'Okiru', 'DDoS', 'C&C', 'FileDownload'
                ]))

        data['label'] = labels
        data['detailed-label'] = detailed_labels

        df = pd.DataFrame(data)

        # Convert boolean columns to int for ML processing
        bool_cols = df.select_dtypes(include=[bool]).columns
        df[bool_cols] = df[bool_cols].astype(int)

        return df

    def load_dataset(self, dataset_name: str, custom_split: float = 0.2) -> Optional[pd.DataFrame]:
        """Load specified dataset"""
        self.dataset_name = dataset_name
        config = self.dataset_configs.get(dataset_name)

        if not config:
            return None

        try:
            if dataset_name == 'UNSW-NB15':
                # Load UNSW-NB15 (existing functionality)
                return self._load_unsw_nb15()

            elif dataset_name == 'IoT-23':
                # Load or simulate IoT-23
                return self._load_iot23()

            elif dataset_name == 'Custom':
                # Load custom dataset
                return self._load_custom()

        except Exception as e:
            return None

    def _load_unsw_nb15(self) -> pd.DataFrame:
        """Load UNSW-NB15 dataset"""
        try:
            # Try to load existing files
            train_df = pd.read_csv('data/raw/UNSW_NB15_training-set.csv')
            test_df = pd.read_csv('data/raw/UNSW_NB15_testing-set.csv')

            self.data = pd.concat([train_df, test_df], ignore_index=True)
            return self.data

        except FileNotFoundError:
            return self._simulate_unsw_nb15()

    def _load_iot23(self) -> pd.DataFrame:
        """Load IoT-23 dataset"""
        try:
            # Try to load actual IoT-23 file
            self.data = pd.read_csv('data/raw/IoT-23.csv')
            return self.data

        except FileNotFoundError:
            self.data = self.simulate_iot23_data()
            return self.data

    def _load_custom(self) -> pd.DataFrame:
        """Load custom dataset"""
        try:
            self.data = pd.read_csv('data/raw/custom_dataset.csv')
            return self.data
        except FileNotFoundError:
            return None

    def _simulate_unsw_nb15(self, n_samples: int = 50000) -> pd.DataFrame:
        """Simulate UNSW-NB15 structure for demonstration"""
        np.random.seed(42)

        # Simulate UNSW-NB15 features
        data = {
            'dur': np.abs(np.random.exponential(1, n_samples)),
            'proto': np.random.choice(['tcp', 'udp', 'icmp'], n_samples),
            'service': np.random.choice(['http', 'ftp', 'smtp', 'ssh', 'dns'], n_samples),
            'state': np.random.choice(['FIN', 'INT', 'CON', 'REQ'], n_samples),
            'spkts': np.abs(np.random.poisson(10, n_samples)),
            'dpkts': np.abs(np.random.poisson(8, n_samples)),
            'sbytes': np.abs(np.random.exponential(1000, n_samples)),
            'dbytes': np.abs(np.random.exponential(500, n_samples)),
            'rate': np.abs(np.random.gamma(2, 2, n_samples)),
            'sttl': np.random.randint(1, 255, n_samples),
            'dttl': np.random.randint(1, 255, n_samples),
            'sload': np.abs(np.random.normal(100, 50, n_samples)),
            'dload': np.abs(np.random.normal(80, 40, n_samples)),
            'sloss': np.abs(np.random.poisson(0.1, n_samples)),
            'dloss': np.abs(np.random.poisson(0.1, n_samples)),
            'sinpkt': np.abs(np.random.exponential(50, n_samples)),
            'dinpkt': np.abs(np.random.exponential(40, n_samples)),
            'sjit': np.abs(np.random.exponential(1, n_samples)),
            'djit': np.abs(np.random.exponential(1, n_samples)),
            'swin': np.random.randint(0, 65535, n_samples),
            'stcpb': np.random.randint(0, 1000000, n_samples),
            'dtcpb': np.random.randint(0, 1000000, n_samples),
            'dwin': np.random.randint(0, 65535, n_samples),
            'tcprtt': np.abs(np.random.exponential(0.1, n_samples)),
            'synack': np.abs(np.random.exponential(0.05, n_samples)),
            'ackdat': np.abs(np.random.exponential(0.05, n_samples)),
            'smean': np.abs(np.random.normal(100, 30, n_samples)),
            'dmean': np.abs(np.random.normal(80, 25, n_samples)),
            'trans_depth': np.random.randint(0, 10, n_samples),
            'response_body_len': np.abs(np.random.exponential(200, n_samples)),
            'ct_srv_src': np.random.randint(1, 100, n_samples),
            'ct_state_ttl': np.random.randint(1, 100, n_samples),
            'ct_dst_ltm': np.random.randint(1, 100, n_samples),
            'ct_src_dport_ltm': np.random.randint(1, 100, n_samples),
            'ct_dst_sport_ltm': np.random.randint(1, 100, n_samples),
            'ct_dst_src_ltm': np.random.randint(1, 100, n_samples),
            'is_ftp_login': np.random.choice([0, 1], n_samples, p=[0.95, 0.05]),
            'ct_ftp_cmd': np.random.randint(0, 10, n_samples),
            'ct_flw_http_mthd': np.random.randint(0, 5, n_samples),
            'ct_src_ltm': np.random.randint(1, 100, n_samples),
            'ct_srv_dst': np.random.randint(1, 100, n_samples),
            'is_sm_ips_ports': np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
        }

        # Create labels
        attack_types = ['Normal', 'DoS', 'Exploits', 'Generic', 'Reconnaissance',
                       'Fuzzers', 'Analysis', 'Backdoor', 'Shellcode', 'Worms']

        data['attack_cat'] = np.random.choice(attack_types, n_samples,
                                            p=[0.7, 0.05, 0.05, 0.05, 0.05, 0.03, 0.02, 0.02, 0.02, 0.01])
        data['label'] = (data['attack_cat'] != 'Normal').astype(int)

        df = pd.DataFrame(data)
        return df

    def create_risk_labels(self):
        """Create risk level labels from attack categories"""
        if self.data is None or self.dataset_name is None:
            return

        config = self.dataset_configs[self.dataset_name]
        risk_mapping = config['risk_mapping']
        attack_col = config['attack_col']

        if attack_col in self.data.columns:
            self.data['risk_level'] = self.data[attack_col].map(risk_mapping)
            self.data['risk_level'] = self.data['risk_level'].fillna('Medium')
        else:
            # Fallback to binary classification
            label_col = config.get('label_col', 'label')
            if label_col in self.data.columns:
                self.data['risk_level'] = self.data[label_col].apply(
                    lambda x: 'High' if x == 1 or x == 'Malware' else 'Low'
                )
            else:
                self.data['risk_level'] = 'Medium'

        risk_dist = self.data['risk_level'].value_counts()

    def prepare_features(self, test_size: float = 0.2, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Prepare features for ML with custom split"""
        if self.data is None or self.dataset_name is None:
            return None, None, None, None

        config = self.dataset_configs[self.dataset_name]
        exclude_cols = config['exclude_cols']

        # Select numeric features
        numeric_cols = []
        for col in self.data.columns:
            if col not in exclude_cols and pd.api.types.is_numeric_dtype(self.data[col]):
                numeric_cols.append(col)

        self.feature_names = numeric_cols

        # Get features and target
        X = self.data[numeric_cols].fillna(0)

        # Encode target
        le = LabelEncoder()
        y = le.fit_transform(self.data['risk_level'])
        self.encoders['risk_level'] = le

        # Custom split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )

        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test

    def get_feature_names(self) -> list:
        """Get list of feature names"""
        return self.feature_names

    def get_risk_level_names(self) -> list:
        """Get risk level class names"""
        if 'risk_level' in self.encoders:
            return self.encoders['risk_level'].classes_.tolist()
        return ['Low', 'Medium', 'High']

    def save_preprocessor(self, path: str = 'models/'):
        """Save fitted preprocessors"""
        os.makedirs(path, exist_ok=True)
        joblib.dump(self.scaler, f'{path}/scaler_{self.dataset_name.lower()}.pkl')
        joblib.dump(self.encoders, f'{path}/encoders_{self.dataset_name.lower()}.pkl')

    def get_dataset_info(self) -> Dict[str, Any]:
        """Get comprehensive dataset information"""
        if self.data is None:
            return {}

        info = {
            'name': self.dataset_name,
            'shape': self.data.shape,
            'features': len(self.feature_names),
            'samples': len(self.data),
            'risk_distribution': self.data['risk_level'].value_counts().to_dict() if 'risk_level' in self.data.columns else {},
            'missing_values': self.data.isnull().sum().sum(),
            'memory_usage': f"{self.data.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB"
        }

        return info


# Test functionality
if __name__ == "__main__":
    loader = EnhancedDataLoader()

    # Test UNSW-NB15
    data = loader.load_dataset('UNSW-NB15')
    if data is not None:
        loader.create_risk_labels()
        X_train, X_test, y_train, y_test = loader.prepare_features(test_size=0.3)

    # Test IoT-23
    data = loader.load_dataset('IoT-23')
    if data is not None:
        loader.create_risk_labels()
        X_train, X_test, y_train, y_test = loader.prepare_features(test_size=0.2)
        info = loader.get_dataset_info()