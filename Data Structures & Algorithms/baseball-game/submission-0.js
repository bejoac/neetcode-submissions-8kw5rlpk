class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        const ans = [];

        while (operations.length != 0) {
            const op = operations.shift();
            
            if (op == "D" && ans.length > 0) {
                ans.push(ans[ans.length - 1] * 2);
            } else if (op == "C" && ans.length > 0) {
                ans.pop();
            } else if (op == "+" && ans.length > 1) {
                const add1 = ans[ans.length - 1];
                const add2 = ans[ans.length - 2];
                ans.push(add1 + add2);
            } else {
                ans.push(parseInt(op));
            };
        };

        let output = 0;

        for (const an of ans) {
            output += an;
        };

        return output;
    };
};
