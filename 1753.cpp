#include <climits>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int INF = INT_MAX;

int main() {
  int V, E, start;
  cin >> V >> E;
  cin >> start;

  // 인접 리스트로 그래프 표현 (메모리 효율적)
  vector<vector<pair<int, int>>> graph(V + 1);

  for (int i = 0; i < E; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    graph[u].push_back({v, w}); // 방향 그래프
  }

  // 거리 배열 초기화
  vector<int> dist(V + 1, INF);
  dist[start] = 0;

  // 우선순위 큐 (거리, 정점) - 최소 힙
  priority_queue<pair<int, int>, vector<pair<int, int>>,
                 greater<pair<int, int>>>
      pq;
  pq.push({0, start});

  while (!pq.empty()) {
    int current_dist = pq.top().first;
    int current_vertex = pq.top().second;
    pq.pop();

    // 이미 처리된 정점이면 스킵
    if (current_dist > dist[current_vertex])
      continue;

    // 인접한 정점들 확인
    for (auto &edge : graph[current_vertex]) {
      int next_vertex = edge.first;
      int weight = edge.second;
      int new_dist = current_dist + weight;

      // 더 짧은 경로를 찾으면 갱신
      if (new_dist < dist[next_vertex]) {
        dist[next_vertex] = new_dist;
        pq.push({new_dist, next_vertex});
      }
    }
  }

  // 결과 출력
  for (int i = 1; i <= V; i++) {
    if (dist[i] == INF) {
      cout << "INF" << endl;
    } else {
      cout << dist[i] << endl;
    }
  }

  return 0;
}