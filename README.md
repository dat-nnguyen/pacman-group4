# Pacman AI — Nhóm 4

- **[Project 1 — Search](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj1/):** tìm đường, thăm bốn góc và thu thập thức ăn trong mê cung.
- **[Project 2 — Multi-Agent](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj2/#welcome-to-multi-agent-pacman):** chọn hành động khi có ma, sử dụng các thuật toán tìm kiếm và hàm đánh giá trạng thái.

## Chuẩn bị

Cần Python 3 có **Tkinter** để mở giao diện; không cần cài thêm thư viện pip. Nếu chưa có `.venv`, tạo bằng `python3 -m venv .venv` với bản Python có Tkinter.

Tại thư mục gốc, kích hoạt môi trường:

```bash
source .venv/bin/activate
```

Các lệnh bên dưới dựa trên hai mô tả chính thức ở đầu README, dùng tên thư mục của repository này. Chạy riêng từng lệnh trong đúng thư mục project; mỗi project có `pacman.py` và `autograder.py` riêng.

- Với `pacman.py`: `-q` tắt giao diện, `-f` cố định ngẫu nhiên, `-n 10` chạy 10 ván, `-k 1` dùng một ma.
- `--frameTime 0` tăng tốc hoạt ảnh; `-z 0.5` thu nhỏ bàn chơi. Nhấn `Ctrl+C` trong terminal để dừng demo.
- Với `autograder.py`, `-q q4` là **chọn câu Q4**; dùng `--no-graphics` để tắt giao diện.

## Project 1 — Search

```bash
cd 'search(project_1)'

# Chơi bằng bàn phím hoặc xem các tùy chọn chạy.
python pacman.py
python pacman.py -h

# Kiểm tra SearchAgent bằng đường đi có sẵn cho tinyMaze.
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

# Q1 (3 pts): Finding a Fixed Food Dot using Depth First Search
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z 0.5 -p SearchAgent

# Q2 (3 pts): Breadth First Search
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z 0.5

# Q3 (3 pts): Varying the Cost Function
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

# Q4 (3 pts): A* search
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# Q5 (3 pts): Finding All the Corners
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# Q6 (3 pts): Corners Problem: Heuristic
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

# Q7 (4 pts): Eating All The Dots
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent

# Q8 (3 pts): Suboptimal Search
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z 0.5
```

Q1–Q6 và Q8 đã hoàn thành. Q7 vẫn trả heuristic bằng `0`, tương đương UCS: chạy được nhưng chưa đạt yêu cầu heuristic có ích. Q3 dùng ba hàm chi phí khác nhau; quan sát `Path found` và `Search nodes expanded` để so sánh chi phí và số trạng thái được mở rộng. Q8 tìm đường nhanh nhưng không đảm bảo tổng hành trình ngắn nhất.

## Project 2 — Multi-Agent

Từ thư mục Project 1, chuyển sang Project 2:

```bash
cd '../multiagent(project_2)'

# Q1 — Reflex Agent
python pacman.py -p ReflexAgent -l testClassic
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 2

# Q2 — Minimax
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4

# Q3 — Alpha-Beta Pruning
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

# Q4 — Expectimax
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10

# Q5 — Evaluation Function
python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better,depth=2 -g RandomGhost -k 1 -f
```

Q1, Q4 và Q5 đã hoàn thành; Q2 và Q3 chưa triển khai. `depth=2` tính hai vòng, mỗi vòng gồm Pacman và tất cả ma. Q4 dùng hàm điểm mặc định; thêm `evalFn=better` để dùng hàm Q5. Thua một ván không đồng nghĩa sai thuật toán; dùng bộ chấm để kiểm tra. Q5 cần được đánh giá qua 10 ván bằng lệnh riêng bên dưới.

## Kiểm tra bằng bộ chấm

Trong thư mục của từng project:

```bash
# Chấm toàn bộ project.
python autograder.py --no-graphics

# Chấm riêng một câu; thay q4 bằng q1–q8 (Project 1) hoặc q1–q5 (Project 2).
python autograder.py -q q4 --no-graphics
```

Chạy một test cụ thể, bỏ phần mở rộng `.test`:

```bash
# Chạy trong search(project_1).
python autograder.py -t test_cases/q7/food_heuristic_1 --no-graphics

# Chạy trong multiagent(project_2).
python autograder.py -t test_cases/q2/0-small-tree --no-graphics

# Chạy trong multiagent(project_2): chấm Q5 qua 10 ván theo bộ chấm.
python autograder.py -q q5 --no-graphics
```

Không sao chép mã hoặc chạy lẫn bộ chấm giữa hai project. Lệnh demo dùng `-f` không thay thế bộ chấm: seed và cấu hình chấm đã được định nghĩa riêng trong `test_cases/`.
