class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def day_of_year(date_str):
            month, day = map(int, date_str.split('-'))
            return sum(days_in_month[:month - 1]) + day
        
        alice_arrive = day_of_year(arriveAlice)
        alice_leave = day_of_year(leaveAlice)
        bob_arrive = day_of_year(arriveBob)
        bob_leave = day_of_year(leaveBob)
        
        start_overlap = max(alice_arrive, bob_arrive)
        end_overlap = min(alice_leave, bob_leave)
        
        return max(0, end_overlap - start_overlap + 1)
