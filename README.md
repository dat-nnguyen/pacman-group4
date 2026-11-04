# Pacman AI — Nhóm 4

- **[Project 1 — Search](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj1/):** tìm đường, thăm bốn góc và thu thập thức ăn trong mê cung.
- **[Project 2 — Multi-Agent](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj2/#welcome-to-multi-agent-pacman):** chọn hành động khi có ma, sử dụng các thuật toán tìm kiếm và hàm đánh giá trạng thái.

## Chuẩn bị

Cần Python 3 có **Tkinter** để mở giao diện; không cần cài thêm thư viện pip. Nếu chưa có `.venv`, tạo bằng `python3 -m venv .venv` với bản Python có Tkinter.

Tại thư mục gốc, kích hoạt môi trường:

```bash
source .venv/bin/activate
```

Chạy riêng từng lệnh demo bên dưới. Thêm `-q` để chạy không mở cửa sổ; `-f` cố định ngẫu nhiên để dễ lặp lại demo.

## Project 1 — Search

```bash
cd 'search(project_1)'

# Q1 (3 pts): Finding a Fixed Food Dot using Depth First Search
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

# Q2 (3 pts): Breadth First Search
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Q3 (3 pts): Varying the Cost Function
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# Q4 (3 pts): A* search
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# Q5 (3 pts): Finding All the Corners
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# Q6 (3 pts): Corners Problem: Heuristic
python pacman.py -l mediumCorners -p AStarCornersAgent

# Q7 (4 pts): Eating All The Dots
python pacman.py -l tinySearch -p AStarFoodSearchAgent

# Q8 (3 pts): Suboptimal Search
python pacman.py -l mediumSearch -p ClosestDotSearchAgent
```

Q1–Q6 và Q8 đã hoàn thành. Q7 thì chưa: demo nhỏ chạy được nhưng chưa đạt yêu cầu tối ưu tìm kiếm. Quan sát `Path found` và `Search nodes expanded` trong terminal để so sánh thuật toán.

## Project 2 — Multi-Agent

Từ thư mục Project 1, chuyển sang Project 2:

```bash
cd '../multiagent(project_2)'

# Q1 (4 pts): Reflex Agent
python pacman.py -l openClassic -p ReflexAgent -g RandomGhost -k 1 -f

# Q2 (5 pts): Minimax
python pacman.py -l minimaxClassic -p MinimaxAgent -a depth=2 -f

# Q3 (5 pts): Alpha-Beta Pruning
python pacman.py -l minimaxClassic -p AlphaBetaAgent -a depth=2 -f

# Q4 (5 pts): Expectimax
python pacman.py -l smallClassic -p ExpectimaxAgent -a depth=2 -g RandomGhost -k 1 -f

# Q5 (6 pts): Evaluation Function
python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better,depth=2 -g RandomGhost -k 1 -f
```

Q1, Q4 và Q5 đã hoàn thành; Q2 và Q3 chưa triển khai. Q4 chấm tính đúng thuật toán, không yêu cầu thắng mọi ván; Q5 đánh giá thêm điểm số và số ván thắng.

## Kiểm tra bằng bộ chấm

Trong thư mục của từng project:

```bash
# Chấm toàn bộ project.
python autograder.py --no-graphics

# Chấm riêng một câu; thay x bằng câu cần kiểm tra.
python autograder.py -q qx --no-graphics
```
