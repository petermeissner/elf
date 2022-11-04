import pytest
import dataelf

def test_testing():
  assert 1==1

def test_package_load():
  dataelf.read_elf()

print("--done--")

