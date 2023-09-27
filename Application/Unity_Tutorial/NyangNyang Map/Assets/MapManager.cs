using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MapManager : MonoBehaviour
{   
    // 타일을 담을 배열 
    // [0][3][6]
    // [1][4][7]
    // [2][5][6]
    [SerializeField] public GameObject[] landArray;
    [SerializeField] public GameObject player;
    // 타일 하나의 크기 = 2.2f
    [SerializeField] public float UnitSize;
    // 플레이어의 이동 속도
    readonly float speed = 50f;
    // 시야; 시야 밖에 타일이 없으면 타일을 갱신
    readonly float halfSight = 1;
    // 전체 타일 크기; 순서대로 왼쪽-위 좌표, 오른쪽-아래 좌표를 담고 있음
    Vector3[] border;

    void Start()
    {
        // border 초기화, 플레이어의 시작 위치는 (0, 1, 0)이므로 왼쪽 끝 좌표는 -UnitSize * 1.5f, 오른쪽 끝 좌표는 UnitSize * 1.5f
        // 둘을 합하면 UnitSize * 3이며 이는 전체 타일의 크기와 같음
        border = new Vector3[]
        {
            new Vector3(-UnitSize * 1.5f, 0, UnitSize * 1.5f),
            new Vector3(UnitSize * 1.5f, 0,  -UnitSize * 1.5f),
        };
    }

    // Update is called once per frame
    void Update()
    {
        // 키 입력이 없으면 업데이트 하지 않음
        if (!Input.anyKey)
            return;

        // 시야 안에 타일이 없는 경우 체크
        BoundaryCheck();
    }

    void BoundaryCheck()
    {
        // 오른쪽에 타일이 없을 경우
        if (border[1].x < player.transform.position.x + halfSight)
        {
            // 타일 영역을 타일 하나 사이즈만큼 오른쪽으로 이동 
            border[0] += Vector3.right * UnitSize;
            border[1] += Vector3.right * UnitSize;

            // 타일을 실제로 오른쪽으로 움직임
            MoveWorld(0);
        }

        // 왼쪽에 타일이 없을 경우
        else if (border[0].x > player.transform.position.x - halfSight)
        {
            border[0] -= Vector3.right * UnitSize;
            border[1] -= Vector3.right * UnitSize;

            MoveWorld(2);
        }

        // 위쪽에 타일이 없을 경우
        else if (border[0].z < player.transform.position.z + halfSight)
        {
            border[0] += Vector3.forward * UnitSize;
            border[1] += Vector3.forward * UnitSize;

            MoveWorld(1);
        }

        // 아래쪽에 타일이 없을 경우
        else if (border[1].z > player.transform.position.z- halfSight)
        {
            border[0] -= Vector3.forward * UnitSize;
            border[1] -= Vector3.forward * UnitSize;

            MoveWorld(3);
        }
    }

    void MoveWorld(int dir)
    {
        // 기존 배열 복사
        // landArray는 새로운 배열, _landArray는 기존 배열을 뜻함
        GameObject[] _landArray = new GameObject[9];
        System.Array.Copy(landArray, _landArray, 9);

        switch (dir)
        {
            case 0:
                for(int i = 0; i < 9; i++)
                {
                    int revise = i - 3;

                    if (revise < 0)
                    {
                        landArray[9 + revise] = _landArray[i];
                        _landArray[i].transform.position += Vector3.right * UnitSize * 3;
                    }
                    else 
                        landArray[revise] = _landArray[i];
                }
                break;
            
            case 1:
                for(int i = 0; i < 9; i++)
                {
                    int revise = i % 3;

                    if (revise == 2)
                    {
                        landArray[i - 2] = _landArray[i];
                        _landArray[i].transform.position += Vector3.forward * UnitSize * 3;
                    }
                    else   
                        landArray[i + 1] = _landArray[i];
                }
                break;
            
            case 2:
                for (int i = 0; i < 9; i++)
                {
                    int revise = i + 3;

                    if (revise > 8)
                    {
                        landArray[revise - 9] = _landArray[i];
                        _landArray[i].transform.position -= Vector3.right * UnitSize * 3;
                    }
                    else
                        landArray[revise] = _landArray[i];
                }
                break;

            case 3:
                for (int i = 0; i < 9; i++)
                {
                    int revise = i % 3;

                    if (revise == 0)
                    {
                        landArray[i + 2] = _landArray[i];
                        _landArray[i].transform.position -= Vector3.forward * UnitSize * 3;
                    } 
                    else 
                        landArray[i - 1] = _landArray[i];
                }
                break;
        }
    }
}
