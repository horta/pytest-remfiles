import os

import pytest


@pytest.mark.remfiles(
    ["http://rest.s3for.me/limix/plink.fam", "http://rest.s3for.me/limix/plink.bed"]
)
def test_2files(remfiles):
    remfiles.chdir()
    assert set(["plink.fam", "plink.bed"]) == set(os.listdir())


@pytest.mark.remfiles(["http://rest.s3for.me/limix/plink.bed"])
def test_1file(remfiles):
    remfiles.chdir()
    assert set(["plink.bed"]) == set(os.listdir())


def test_nofiles(remfiles):
    remfiles.chdir()
    assert set() == set(os.listdir())


def test_sem_nada(remfiles):
    olddir = os.getcwd()
    remfiles.chdir()
    newdir = os.getcwd()
    assert olddir != newdir
