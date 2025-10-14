import pytest
from hash_table import HashTable

def test_insert_and_get():
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    assert ht.get("apple") == 10
    assert ht.get("banana") == 20
    assert ht.get("orange") is None

def test_update_existing_key():
    ht = HashTable()
    ht.insert("key", 1)
    ht.insert("key", 2)
    assert ht.get("key") == 2
    assert len(ht) == 1

def test_remove_key():
    ht = HashTable()
    ht.insert("a", 1)
    ht.insert("b", 2)
    assert ht.remove("a") is True
    assert ht.get("a") is None
    assert len(ht) == 1
    assert ht.remove("nonexistent") is False

def test_resize():
    ht = HashTable(capacity=2)
    for i in range(10):
        ht.insert(f"key{i}", i)
    assert len(ht) == 10
    assert ht.capacity >= 8
    assert ht.get("key5") == 5

def test_contains():
    ht = HashTable()
    ht.insert("x", 100)
    assert "x" in ht
    assert "y" not in ht
