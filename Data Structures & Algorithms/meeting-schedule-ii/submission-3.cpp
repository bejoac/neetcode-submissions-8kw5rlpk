/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int counter = 0;
        int res = 0;
        
        vector<int> start;
        vector<int> end;
    
        for (Interval interval : intervals) {
            start.push_back(interval.start);
            end.push_back(interval.end);
        };
        
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        
        int s = 0;
        int e = 0;
        
        while (s < start.size()) {
            if (start[s] < end[e]) {
                counter++;
                s++;
            } else {
                counter--;
                e++;
            };
            
            res = max(res, counter);
        };
        
        return res;
    };
};

