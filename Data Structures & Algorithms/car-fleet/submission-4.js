class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        if (position.length !== speed.length) {
            return false;
        };
        
        const positionAndSpeed = [];
        const stack = [];

        for (let i = 0; i < position.length; i++) {
            positionAndSpeed.push([position[i], speed[i]])
        };

        positionAndSpeed.sort((a, b) => b[0] - a[0]);

        for (const [p, s] of positionAndSpeed) {
            stack.push((target - p) / s);

            if (stack.length >= 2 && (stack[stack.length - 1] <= stack[stack.length - 2])) {
                stack.pop();
            };
        };

        return stack.length;
    };
}
