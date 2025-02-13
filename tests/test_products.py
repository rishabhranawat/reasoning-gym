import pytest

from reasoning_gym.arithmetic import Products, ProductsConfig
from reasoning_gym.arithmetic.products import ProductsCurriculum


def test_products_config_validation():
    """Test that invalid configs raise appropriate errors"""
    with pytest.raises(AssertionError):
        config = ProductsConfig(min_terms=0)
        config.validate()

    with pytest.raises(AssertionError):
        config = ProductsConfig(min_terms=3, max_terms=2)
        config.validate()


def test_products_deterministic():
    """Test that dataset generates same items with same seed"""
    config = ProductsConfig(seed=42, size=10)
    dataset1 = Products(config)
    dataset2 = Products(config)

    for i in range(len(dataset1)):
        assert dataset1[i] == dataset2[i]


def test_products_items():
    """Test basic properties of generated items"""
    config = ProductsConfig(min_terms=2, max_terms=4, min_digits=1, max_digits=2, size=100, seed=42)
    dataset = Products(config)

    for i in range(len(dataset)):
        item = dataset[i]
        assert isinstance(item, dict)
        assert "question" in item
        assert "answer" in item
        assert "metadata" in item

        # Verify only * is used
        expression = item["metadata"]["expression"]
        assert all(op in ["*", " "] or op.isdigit() for op in expression)

        # Verify the answer matches the expression
        answer = eval(expression)  # Safe here as we control the expression
        assert str(answer) == item["answer"]


def test_products_number_ranges():
    """Test that generated numbers respect digit constraints"""
    # Test 3-digit numbers
    config = ProductsConfig(
        min_terms=2,
        max_terms=2,  # Fix to 2 terms for easier testing
        min_digits=3,  # Should generate numbers >= 100
        max_digits=3,  # Should generate numbers <= 999
        size=50,
        seed=42,
    )
    dataset = Products(config)

    for i in range(len(dataset)):
        item = dataset[i]
        expression = item["metadata"]["expression"]
        numbers = [int(n) for n in expression.split() if n.isdigit()]
        for num in numbers:
            assert 100 <= num <= 999, f"Number {num} outside valid range for 3 digits"

    # Test 1-digit numbers
    config = ProductsConfig(min_terms=2, max_terms=2, min_digits=1, max_digits=1, size=50, seed=42)
    dataset = Products(config)
    for i in range(len(dataset)):
        item = dataset[i]
        expression = item["metadata"]["expression"]
        numbers = [int(n) for n in expression.split() if n.isdigit()]
        for num in numbers:
            assert 0 <= num <= 9, f"Number {num} outside valid range for 1 digit"


def test_products_iteration():
    """Test that iteration respects dataset size"""
    config = ProductsConfig(min_terms=2, max_terms=2, size=5, seed=42)  # Small size for testing
    dataset = Products(config)

    # Test manual iteration
    items = []
    for item in dataset:
        items.append(item)
    assert len(items) == config.size, "Iterator should yield exactly size items"

    # Test list conversion
    items = list(dataset)
    assert len(items) == config.size, "Iterator should yield exactly size items"

    # Test multiple iterations
    first_items = list(dataset)
    second_items = list(dataset)
    assert first_items == second_items, "Multiple iterations should yield same items"


def test_products_curriculum():
    curriculum = ProductsCurriculum()

    base_value = {"size": 150, "seed": 1}

    base_cfg: ProductsConfig = curriculum.generate_configuration(base_value)
    assert base_cfg.seed == 1
    assert base_cfg.size == 150
    assert base_cfg.min_digits == 1 and base_cfg.max_digits == 1
    assert base_cfg.min_terms == 2 and base_cfg.max_terms == 2

    # test incrementing attribute levels for num_terms & num_digits attributes
    curriculum.increment_attr_level("num_terms")
    curriculum.increment_attr_level("num_digits")

    increased_cfg = curriculum.generate_configuration(base_value)
    assert increased_cfg.min_digits == 1 and increased_cfg.max_digits == 2
    assert increased_cfg.min_terms == 2 and increased_cfg.max_terms == 3

    # test decrementing attribute level for num_digits again
    curriculum.decrement_attr_level("num_digits")

    partially_decreased_cfg = curriculum.generate_configuration(base_value)
    assert partially_decreased_cfg.min_digits == 1 and partially_decreased_cfg.max_digits == 1
    assert partially_decreased_cfg.min_terms == 2 and partially_decreased_cfg.max_terms == 3
