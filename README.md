# [🎯🎈 Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150)
### 🌤️ Story
A festive sky is filled with colorful 🎈 balloons floating at different heights. Since they're attached to a giant flat wall, you can't tell how high each balloon is—but you do know how wide each one stretches along the x-axis.

Your mission? *Grab your bow 🏹 and pop **every balloon** using as **few arrows** as possible!*

### 📝 Problem Statement
Each balloon is represented by an interval: **`[xstart, xend]`**, where:
- 📍 **`xstart`** is the leftmost point of the balloon.
- 📍 **`xend`** is the rightmost point of the balloon.

This means the balloon occupies **every x-coordinate between** **`xstart`** and **`xend`** (inclusive).

The balloons may appear at different heights, but **their y-coordinates are unknown and don't affect the problem**.

#### 🏹 How Do the Arrows Work?

You can shoot arrows **straight upward** from **any x-coordinate** on the x-axis.

Every arrow:
- ⬆️ Travels upward forever.
- 💥 Bursts every balloon that lies in its vertical path.
- 🎯 Can burst **multiple balloons** if they all cover the arrow's x-coordinate.

A balloon **`[xstart, xend]`** is burst if the arrow is fired at position **`x`** where: **`xstart ≤ x ≤ xend`**

Even firing exactly at **xstart** or **xend** will burst the balloon.

#### 🎯 Your Mission

*Find the **minimum number of arrows** needed to burst **every balloon**.*

Remember:
- 🤝 Overlapping balloons can often be burst together.
- 🚫 Non-overlapping balloons usually require separate arrows.
- 🎈 Every balloon must be popped.

#### 📚 Examples
**🎈 Example 1 — One Arrow, Two Balloons!**
```
points = [[10,16],[2,8],[1,6],[7,12]]
output = 2
```
**Explanation :** <br>
The first arrow 🏹 is fired at **x = 6**, bursting: <br> 🎈 **`[2,8]`** <br> 🎈 **`[1,6]`** <br> The second arrow 🏹 is fired at **x = 11**, bursting: <br> 🎈 **`[10,16]`** <br> 🎈 **`[7,12]`** <br >✨ Only **2 arrows** are enough to burst all four balloons.

**🎈 Example 2 — Every Balloon Stands Alone**
```
points = [[1,2],[3,4],[5,6],[7,8]]
output = 4
```
**Explanation :** <br> None of the balloons overlap. Each balloon needs its own arrow, so: <br> 🏹 ➜ 🎈 <br> 🏹 ➜ 🎈 <br> 🏹 ➜ 🎈 <br> 🏹 ➜ 🎈 <br> Total arrows required: **4**

**🎈 Example 3 — Touching Counts!**
```
points = [[1,2],[2,3],[3,4],[4,5]]
output = 2
```
**Explanation :** <br> The first arrow 🏹 is fired at **x = 2**, bursting: <br> 🎈 [1,2] <br> 🎈 [2,3] <br> The second arrow 🏹 is fired at **x = 4**, bursting: <br> 🎈 [3,4] <br>🎈 [4,5] <br> Because the interval endpoints are **inclusive**, balloons that **touch at a boundary** can still be burst by the same arrow.

#### 📌 Constraints
- 📦 **`1 ≤ points.length ≤ 10⁵`**
- 📦 **`points[i].length == 2`**
- 📍 **`-2³¹ ≤ xstart < xend ≤ 2³¹ - 1`**

#### 💡 Things to Remember
- 🎈 Balloons can overlap completely, partially, or not at all.
- 🏹 One arrow can burst **many balloons** if they all cover the same x-coordinate.
- 📍 You may shoot an arrow from **any x-coordinate**.
- ⬆️ Arrows travel infinitely upward.
- 🎯 Your goal is **only** to determine the **minimum number of arrows** required to burst every balloon—not the exact positions where they should be fired.
---
### 🏹 Approach: Greedy Interval Strategy 🎈
#### 💡 Intuition
Imagine you are standing in front of a wall filled with balloons 🎈. Each balloon covers a horizontal range on the x-axis, and an arrow shot at a specific x-coordinate can burst every balloon that includes that position.

The goal is not to find ***where every arrow should be shot***, but to find the ***minimum number of arrows needed***.

The key observation is:
> 🎯 If we always shoot an arrow at the position where a balloon ends earliest, we maximize the chance of bursting other overlapping balloons with the same arrow.

Why? 🤔
- A balloon with a smaller ending coordinate gives us the **least flexibility**.
- Placing an arrow at this earliest ending point keeps it inside the current balloon.
- Any future balloon that overlaps this position can also be burst by the same arrow.
- If a future balloon starts after this position, it cannot be burst by the current arrow, so we need a new one.

This transforms the problem into a classic ***Greedy Interval Scheduling problem***. 🚀

#### 🧠 Step-by-Step Explanation
**1️⃣ Sort Balloons by Their Ending Position 🎈** <br>
First, arrange all balloons based on their **`xend`** value. <br> Example: <br> **Before sorting :** **`[[10,16],[2,8],[1,6],[7,12]]`** <br> **After sorting by ending coordinate :** **`[[1,6],[2,8],[7,12],[10,16]]`** <br> 🎯 Why sort by ending position? <br> Because the balloon that ends earliest gives us the best possible arrow position to cover future overlapping balloons.

**2️⃣ Fire the First Arrow 🏹** <br> Place the first arrow at the ending coordinate of the first balloon. <br> Example: <br> **Balloon :** **`[1,6]`** <br> **Position :** **`1 -------- 🏹 -------- 6`** <br> The arrow is guaranteed to burst this balloon. <br> We store this arrow position because future balloons can potentially share this arrow.

**3️⃣ Check Remaining Balloons 🔍** <br> Now examine each balloon one by one. <br> For every balloon: <br><br> 
> **Case 1: Current Arrow Can Burst It 🎯** <br> If: **`arrow_position >= balloon_start`** <br> then the balloon overlaps with the arrow. <br> Example: <br> **Arrow position : `6`** <br> **Balloon : `🏹 -------- 2 -------- 6 -------- 8`** <br> The balloon is already covered. <br> ✅ No new arrow needed. <br><br> **Case 2: Current Arrow Cannot Reach It 🚫** <br> If: **`arrow_position < balloon_start`** <br> then the balloon starts after our arrow position. <br> Example: <br> **Arrow position : `6`** <br> **Balloon : `7 -------- 12`** <br> There is no overlap.

We must: <br>**1.** 🏹 Fire another arrow. <br> **2.** 🎯 Place it at this balloon's ending coordinate. <br>**3.** Continue checking the remaining balloons. 

**4️⃣ Return Total Arrows 🎉** <br>After processing every balloon, the count represents the minimum number of arrows required.

#### 📝 Pseudocode
```
function findMinimumArrows(points):

    🏹 arrows = 1

    🎈 Sort balloons by ending coordinate

    🎯 arrowPosition = end of first balloon


    for each balloon from second balloon onwards:

        if arrowPosition < balloon.start:

            🏹 Need another arrow
            arrows += 1

            🎯 Move arrow to balloon.end


    return arrows
```

#### ⏱️ Complexity Analysis
**🕒 Time Complexity: `O(n log n)`** <br> - Sorting balloons: `O(n log n)` <br> - Traversing balloons once: `O(n)` <br> - Total: **`O(n log n)`**

**💾 Space Complexity: `O(1)`** <br> The algorithm only stores: <br> - 🏹 Current arrow position <br> - 🎯 Arrow count <br> - 🔍 Loop variables <br> No additional data structures are created (*Ignoring the sorting space used internally by the language*).

#### 📊 Approach Summary
| Step | Action                                 | Purpose                                |
| ---- | -------------------------------------- | -------------------------------------- |
| 1️⃣  | Sort balloons by ending position       | Find the best arrow placement order 🎈 |
| 2️⃣  | Shoot arrow at earliest ending balloon | Maximize overlap coverage 🏹           |
| 3️⃣  | Check overlapping balloons             | Reuse existing arrows 🎯               |
| 4️⃣  | Shoot new arrow when needed            | Handle independent balloon groups 💥   |

#### 🌟 Key Takeaway
The greedy idea is simple:
> ***🎯 Always shoot the arrow at the earliest possible ending point, because it gives the maximum chance of bursting future overlapping balloons. 🏹🎈***

This ensures every arrow covers the largest possible group of balloons while keeping the total number of arrows minimal. 🚀

---