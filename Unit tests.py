class FloydTestCase(unittest.TestCase):
    def test_floyd(self):
        expected_result = [[0, 7, 12, 8],
                           [NO_PATH, 0, 5, 7],
                           [NO_PATH, NO_PATH, 0, 2],
                           [NO_PATH, NO_PATH, NO_PATH, 0]]

        result = floyd_warshall(graph)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
