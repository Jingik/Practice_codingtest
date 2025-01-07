#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 회의 정보를 저장할 구조체
struct Meeting {
    int start;
    int end;
};

// 끝나는 시간을 기준으로 정렬
bool compare(Meeting a, Meeting b) {
    if (a.end == b.end) return a.start < b.start;
    return a.end < b.end;
}

int main() {
    int n;
    cin >> n;

    vector<Meeting> meetings(n);

    // 입력 받기
    for (int i = 0; i < n; i++) {
        cin >> meetings[i].start >> meetings[i].end;
    }

    // 끝나는 시간을 기준으로 정렬
    sort(meetings.begin(), meetings.end(), compare);

    int count = 0; // 사용할 수 있는 최대 회의 개수
    int end_time = 0; // 마지막 회의의 끝나는 시간

    for (int i = 0; i < n; i++) {
        // 현재 회의가 이전 회의와 겹치지 않으면 선택
        if (meetings[i].start >= end_time) {
            end_time = meetings[i].end;
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
