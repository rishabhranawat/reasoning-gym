"""
Arithmetic tasks for training reasoning capabilities:
"""

from .basic_arithmetic import BasicArithmeticDataset, BasicArithmeticDatasetConfig
from .calendar_arithmetic import CalendarArithmeticConfig, CalendarArithmeticDataset
from .chain_sum import ChainSumConfig, ChainSumDataset
from .count_bits import CountBitsConfig, CountBitsDataset
from .dice import DiceConfig, DiceDataset
from .fraction_simplification import FractionSimplificationConfig, FractionSimplificationDataset
from .gcd import GCDConfig, GCDDataset
from .gsm_symbolic.gsm_symbolic import GSMSymbolicDataset, GSMSymbolicDatasetConfig
from .lcm import LCMConfig, LCMDataset
from .leg_counting import LegCountingConfig, LegCountingDataset
from .power_function import PowerFunctionConfig, PowerFunctionDataset
from .prime_factorization import PrimeFactorizationConfig, PrimeFactorizationDataset
from .products import ProductsConfig, ProductsDataset
from .time_intervals import TimeIntervalsConfig, TimeIntervalsDataset

__all__ = [
    "BasicArithmeticDataset",
    "BasicArithmeticDatasetConfig",
    "ChainSumDataset",
    "ChainSumConfig",
    "CalendarArithmeticConfig",
    "CalendarArithmeticDataset",
    "FractionSimplificationConfig",
    "FractionSimplificationDataset",
    "GCDConfig",
    "GCDDataset",
    "LCMConfig",
    "LCMDataset",
    "LegCountingConfig",
    "LegCountingDataset",
    "PowerFunctionConfig",
    "PowerFunctionDataset",
    "PrimeFactorizationConfig",
    "PrimeFactorizationDataset",
    "ProductsDataset",
    "ProductsConfig",
    "GSMSymbolicDatasetConfig",
    "GSMSymbolicDataset",
    "TimeIntervalsConfig",
    "TimeIntervalsDataset",
    "CountBitsConfig",
    "CountBitsDataset",
    "DiceConfig",
    "DiceDataset",
]
