import pytest
import random


class TestAbc:
    @pytest.mark.run(order=-1)
    def test_a(self):
        assert 1

    @pytest.mark.run(order=1)
    def test_b(self):
        assert 1

    @pytest.mark.run(order=1)
    def test_e(self):
        assert 1

    @pytest.mark.run(order=1)
    def test_f(self):
        assert 1

    @pytest.mark.skipif(True,reason='C完成')
    def test_c(self):
        assert 1

    def test_d(self):
        num = random.randint(1,3)
        if num != 1:
            assert 0
        else:
            assert 1
