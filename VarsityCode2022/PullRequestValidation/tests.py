from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299,52" ]), True)

    def test2(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x5fc,1005-fix-fixed bugs,4191399,29", "0x5fd,-fix-fixed UI,9109344,011" ]), False)

    def test3(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10c,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299,52" ]), False)

    def test4(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,-2999-feat-added UI Buttons,1234299,52" ]), True)
    def test5(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-addedU-I Buttons,1234299,52" ]), True)
    def test6(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,-2999-feat-added UI- Buttons,1234299,52" ]), True)
    def test7(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,0099-feat-added UI Buttons,1234299,52" ]), True)
    def test8(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-charo-added UI Buttons,1234299,52" ]), False)
    def test9(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-,1234299,52" ]), False)
    def test10(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat- ", "52" ]), False)
    def test11(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299,51" ]), False)
    def test12(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299,bb" ]), False)   
    def test13(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,123429l9,52" ]), False)  
    def test14(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341"]), True)  
    def test15(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,301-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299,52" ]), False) 
    def test16(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,0x10-feat-added UI Buttons,1234299,52" ]), False)
    def test17(self):
        result = Solution()
        self.assertEqual(result.verifypr([  ]), False)
    def test18(self):
        result = Solution()
        self.assertEqual(result.verifypr([ "0x10a,3012-chore-updating Dependencies,9019222,341", "0x10b,3012-fix-fixed Errors Resulting From Dependency Update,1231099,741", "0x10c,2999-feat-added UI Buttons,1234299" ]), False)
if __name__ == '__main__':
    unittest.main()