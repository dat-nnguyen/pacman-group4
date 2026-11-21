# Pacman AI — Nhóm 4

- **[Project 1 — Search](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj1/):** tìm đường, thăm bốn góc và thu thập thức ăn trong mê cung.
- **[Project 2 — Multi-Agent](https://inst.eecs.berkeley.edu/~cs188/archive/fa25/projects/proj2/#welcome-to-multi-agent-pacman):** chọn hành động khi có ma, sử dụng các thuật toán tìm kiếm và hàm đánh giá trạng thái.

## Chuẩn bị

Cần Python 3 có **Tkinter** để mở giao diện; không cần cài thêm thư viện pip. Nếu chưa có `.venv`, tạo bằng `python3 -m venv .venv` với bản Python có Tkinter. Môi trường kiểm thử của nhóm dùng Python 3.13.5.

Tại thư mục gốc, kích hoạt môi trường:

```bash
source .venv/bin/activate

# Kiểm tra Python trong môi trường đã có Tkinter.
python -c "import tkinter; print('Tkinter:', tkinter.TkVersion)"
```

Các lệnh bên dưới dựa trên hai mô tả chính thức ở đầu README, dùng tên thư mục của repository này. Chạy riêng từng lệnh trong đúng thư mục project; mỗi project có `pacman.py` và `autograder.py` riêng.

**Không chạy `python pacman.py` tại thư mục gốc** vì file này nằm trong từng project. `.venv` vẫn có hiệu lực sau khi đổi thư mục; khi mở terminal mới, kích hoạt lại từ thư mục gốc. Dùng `deactivate` để thoát môi trường.

- Với `pacman.py`: `-q` tắt giao diện, `-f` cố định ngẫu nhiên, `-n 10` chạy 10 ván, `-k 1` dùng một ma.
- `--frameTime 0` tăng tốc hoạt ảnh; `-z 0.5` thu nhỏ bàn chơi. Nhấn `Ctrl+C` trong terminal để dừng demo.
- Với `autograder.py`, `-q q4` là **chọn câu Q4**; dùng `--no-graphics` để tắt giao diện.
- `-p` chọn agent, `-l` chọn bản đồ, `-a` truyền cấu hình như `depth=2` hoặc `evalFn=better`. Xem mọi tùy chọn bằng `python pacman.py -h` trong thư mục project.

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
python autograder.py -q q1 --no-graphics

# Q2 (3 pts): Breadth First Search
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z 0.5
python autograder.py -q q2 --no-graphics

# Q3 (3 pts): Varying the Cost Function
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python autograder.py -q q3 --no-graphics

# Q4 (3 pts): A* search
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python autograder.py -q q4 --no-graphics

# Q5 (3 pts): Finding All the Corners
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python autograder.py -q q5 --no-graphics

# Q6 (3 pts): Corners Problem: Heuristic
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python autograder.py -q q6 --no-graphics

# Q7 (4 pts): Eating All The Dots
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l tinySearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python autograder.py -q q7 --no-graphics

# Q8 (3 pts): Suboptimal Search
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z 0.5
python autograder.py -q q8 --no-graphics
```

Q1–Q8 đã có cài đặt. Q3 dùng ba hàm chi phí khác nhau; quan sát `Path found` và `Search nodes expanded` để so sánh chi phí và số trạng thái được mở rộng. Q7 dùng khoảng cách Manhattan lớn nhất giữa các cặp điểm gồm Pacman và thức ăn còn lại. Q8 tìm đường nhanh nhưng không đảm bảo tổng hành trình ngắn nhất; `Path found with cost 350` là tổng số bước trên `bigSearch`. Log khởi tạo Q8 có thể ghi DFS do kế thừa lớp cha, nhưng hàm tìm thức ăn thực tế gọi BFS.

## Project 2 — Multi-Agent

Từ thư mục Project 1, chuyển sang Project 2:

Nếu đang ở thư mục gốc thay vì Project 1, dùng `cd 'multiagent(project_2)'` thay cho lệnh `cd` đầu tiên bên dưới.

```bash
cd '../multiagent(project_2)'

# Q1 — Reflex Agent
python pacman.py -p ReflexAgent -l testClassic
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 2
python autograder.py -q q1 --no-graphics

# Q2 — Minimax
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
python autograder.py -q q2 --no-graphics

# Q3 — Alpha-Beta Pruning
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
python pacman.py -p AlphaBetaAgent -l minimaxClassic -a depth=4
python autograder.py -q q3 --no-graphics

# Q4 — Expectimax
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10

# So sánh với Alpha-Beta trên cùng bản đồ, cùng độ sâu và số ván.
python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10

# Demo Q4 trên bản đồ rộng hơn với hai ma.
python pacman.py -p ExpectimaxAgent -l smallClassic -a depth=2 -k 2 -f
python autograder.py -q q4 --no-graphics

# Q5 (6 pts): Evaluation Function
python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better,depth=2 -g RandomGhost -k 1 -f

# Kết hợp Q4 và Q5 trên mediumClassic với hai ma.
python pacman.py -p ExpectimaxAgent -l mediumClassic -a evalFn=better,depth=2 -k 2 -f

# Chạy nhanh 10 ván Q5; dùng autograder để đối chiếu kết quả chấm chính thức.
python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better,depth=2 -g RandomGhost -k 1 -n 10 -q -f
python autograder.py -q q5 --no-graphics
```

Q1–Q5 đã có cài đặt. `depth=2` tính hai vòng, mỗi vòng gồm Pacman và tất cả ma. Q4 dùng hàm điểm mặc định; thêm `evalFn=better` để dùng hàm Q5. Tăng độ sâu hoặc số ma làm cây tìm kiếm lớn hơn và chạy chậm hơn. Thua một ván không đồng nghĩa sai thuật toán; dùng bộ chấm để kiểm tra. Để xem đồ họa của kịch bản `trappedClassic`, bỏ `-q`; để chỉ chạy một ván, bỏ thêm `-n 10`.

## Kiểm tra bằng bộ chấm

Trong thư mục của từng project:

```bash
# Chấm toàn bộ project.
python autograder.py --no-graphics

# Chấm riêng một câu; thay q4 bằng q1–q8 (Project 1) hoặc q1–q5 (Project 2).
python autograder.py -q q4 --no-graphics
```

Hoặc từ thư mục gốc, sau khi kích hoạt `.venv`, chạy toàn bộ hai project lần lượt:

```bash
(cd 'search(project_1)' && python -B autograder.py --no-graphics)
(cd 'multiagent(project_2)' && python -B autograder.py --no-graphics)
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

## Kết quả kiểm thử

Đã chạy toàn bộ bộ chấm của mỗi project một lượt ngày **21/11/2026**, bằng Python **3.13.5**, với `--no-graphics`.

| Câu | Project 1 | Project 2 |
|---|---:|---:|
| Q1 | 3/3 | 4/4 |
| Q2 | 3/3 | 5/5 |
| Q3 | 3/3 | 5/5 |
| Q4 | 3/3 | 5/5 |
| Q5 | 3/3 | 6/6 |
| Q6 | 3/3 | — |
| Q7 | 4/4 | — |
| Q8 | 3/3 | — |
| **Tổng** | **25/25** | **25/25** |

- Project 1 Q7 mở rộng **8.763 trạng thái** trên `trickySearch`, đạt đầy đủ **4/4 điểm**. Log vẫn có nhãn `FAIL` ở test hiệu năng vì chưa chạm mốc thưởng thêm **7.000**; không phải toàn bộ Q7 bị đánh trượt.
- Project 2 Q1 thắng **10/10**, trung bình **1257,7** điểm; Q5 thắng **10/10**, trung bình **1132,9** điểm.
- Các ván kiểm thử Q2–Q4 Project 2 có thể thua nhưng vẫn đạt điểm thuật toán. Các ván demo có thể cho kết quả khác khi đổi seed, độ sâu, bản đồ hoặc số ma.

Log đầy đủ: [Project 1](test-results/2026-11-21/search.log), [Project 2](test-results/2026-11-21/multiagent.log).
