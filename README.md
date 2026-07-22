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

### 📚 Examples
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