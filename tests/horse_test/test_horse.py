# coding=utf-8
#
# Guilherme Lima 21/12/16
from tests import base
from horse.knightmoves import go_horse, movimentos_cavalo, input_origem, input_saida
import mock
import __builtin__


class Cavalo(base.TestCase):
    @mock.patch.object(__builtin__, 'raw_input')
    def test_origem(self, mock_raw_input):
        mock_raw_input.return_value = '1,1'
        self.assertEqual(input_origem(), (1, 1))

    @mock.patch.object(__builtin__, 'raw_input')
    def test_origem(self, mock_raw_input):
        mock_raw_input.return_value = '1,1'
        self.assertEqual(input_saida(), (1, 1))

    def test_movimento_cavalo(self):
        movimentos_cavalo.return_value = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

    def test_go_horse(self):
        go_horse([1, 1], [1, 1]).should.be.equal([[0, 3], [1, 1]])
