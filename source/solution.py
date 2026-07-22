from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ''' 🏹 We need at least one arrow because the input contains at least one balloon. '''
        minimum_arrows_needed: int = 1

        '''
         🎈 Sort balloons by their ending position.
        
         🎯 Choosing the balloon with the earliest ending point helps us
         place arrows strategically so that the same arrow can burst
         as many overlapping balloons as possible.
        
         Example:
         Before sorting:
         [[10,16], [2,8], [1,6], [7,12]]
        
         After sorting:
         [[1,6], [2,8], [7,12], [10,16]]
        '''
        points.sort(key=lambda balloon: balloon[1])

        '''
         🏹 Fire the first arrow at the end of the first balloon.
        
         Since the balloons are sorted by their ending coordinates,
         this position gives the arrow maximum overlap potential.
        '''
        last_arrow_position: int = points[0][1]

        '''
         🚶 Check each remaining balloon to see if the current arrow
         can still burst it.
        '''
        for balloon_index in range(1, len(points)):

            ''' 🎈 Extract the current balloon's horizontal range. '''
            balloon_start: int = points[balloon_index][0]
            balloon_end: int = points[balloon_index][1]

            '''
             🔍 If the current arrow is placed before this balloon starts,
             there is no overlap between them.
            
             Example:
             Arrow position: 5
             Balloon range:  [7,12]
            
             5 ❌ -------- 🎈 7 -------- 12
            
             The current arrow cannot burst this balloon,
             so we need another arrow.
            '''
            if last_arrow_position < balloon_start:

                # 🏹 Fire a new arrow for this independent balloon group.
                minimum_arrows_needed += 1

                '''
                 🎯 Place the new arrow at this balloon's ending position.
                
                 This gives future balloons the best chance to overlap
                 with the current arrow.
                '''
                last_arrow_position = balloon_end

            '''
             💥 Otherwise, the current balloon overlaps with the existing arrow.
            
             Example:
             Arrow position: 6
             Balloon range:  [2,8]
            
             2 -------- 🏹 6 -------- 8
            
             The balloon gets burst automatically,
             so no additional arrow is required.
            '''

        ''' 🎉 Return the minimum number of arrows needed to burst all balloons. '''
        return minimum_arrows_needed