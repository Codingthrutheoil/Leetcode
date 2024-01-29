class MyQueue(object):

    def __init__(self):
        self.list_nums = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list_nums.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.list_nums.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.list_nums[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.list_nums)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()