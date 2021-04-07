//
// Created by 박정무 on 2021/04/07.
//

#include <iostream>
#include <vector>

using namespace std;

int white_blue[2] = {0,0};

void recur(vector<vector<int>> &v,int horizonIndex, int verticalIndex, int squareSize){
    if(squareSize == 1){
        //인덱스의 종이 숫자++
        white_blue[v[verticalIndex][horizonIndex]] ++;
        return;
    }

    // 종이 검사하기
    int beforeValue = v[verticalIndex][horizonIndex];
    for(int i=0;i<squareSize;i++){
        for(int j=0;j<squareSize;j++){
            // 이전값과 같으면??
            if(beforeValue == v[verticalIndex+i][horizonIndex+j]) {
                if(i==squareSize-1 && j==squareSize-1){
                    //검색이 끝나면 종이 ++
                    white_blue[beforeValue]++;
                }
                //이전값 갱신!
                beforeValue = v[verticalIndex+i][horizonIndex+j];
            }
            else{
                //재귀는 1사분면, 2사분면, 3사분면, 4사분면 4개!
                recur(v,horizonIndex,verticalIndex,squareSize/2);
                recur(v,horizonIndex+(squareSize/2),verticalIndex,squareSize/2);
                recur(v,horizonIndex,verticalIndex+(squareSize/2),squareSize/2);
                recur(v,horizonIndex+(squareSize/2),verticalIndex+(squareSize/2),squareSize/2);
                return;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;

    vector<vector<int>> v(t,vector<int>(t,0));

    for(int i=0;i<t;i++) {
        for (int j = 0; j < t; j++) {
            cin >> v[i][j];
        }
    }

    recur(v,0,0,t);
    cout<<white_blue[0]<<"\n"<<white_blue[1];
    return 0;
}
