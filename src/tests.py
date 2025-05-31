import unittest
from main import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(0,0, 20, 20, 50, 50)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        self.assertEqual(
            len(m2._Maze__cells),
            20
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            20
        )
    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Test entrance (top-left cell)
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        
        # Test exit (bottom-right cell)
        self.assertFalse(m._Maze__cells[-1][-1].has_bottom_wall)
        
        # Verify other walls still exist
        self.assertTrue(m._Maze__cells[0][0].has_bottom_wall)
        self.assertTrue(m._Maze__cells[-1][-1].has_top_wall)


if __name__ == "__main__":
    unittest.main()