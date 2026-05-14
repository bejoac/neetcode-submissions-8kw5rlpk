#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

class TimeMap {
    public:
        std::unordered_map<std::string, std::vector<std::pair<std::string, int>>> store = {
            {"Test", {{"Test", 1}, {"Test", 2}}}   
        };
        
        void set(std::string key, std::string value, int timestamp) {
            if (store.count(key)) {
                store[key].push_back({value, timestamp});    
            } else {
                store[key] = {{value, timestamp}};
            };
        };
        
        std::string get(std::string key, int timestamp) {
            std::string res = ""; 
            
            if (store.count(key) == 0) {
                return res;
            };
            
            std::vector values = store[key];
            int l = 0;
            int r = values.size() - 1;
            int m;
            
            while (l <= r) {
                m = l + (r - l) / 2;
                if (timestamp >= values[m].second) {
                    res = values[m].first;
                    l = m + 1;
                } else {
                    r = m - 1;
                };
            };
            
            return res;

        };
};