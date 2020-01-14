import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Card, Icon, Grid, Progress, Message, Step } from 'semantic-ui-react'
import alone from '../image/fig_alon.png'
import anxi from '../image/fig_anxi.png'
import bother from '../image/fig_bother.png'
import capa from '../image/fig_capa.png'
import cold from '../image/fig_cold.png'
import cry from '../image/fig_cry.png'
import depr from '../image/fig_depr.png'
import fail from '../image/fig_fail.png'
import fear from '../image/fig_fear.png'
import fun from '../image/fig_fun.png'
import glo from '../image/fig_glo.png'
import hap from '../image/fig_hap.png'
import hard from '../image/fig_hard.png'
import hate from '../image/fig_hate.png'
import hope from '../image/fig_hope.png'
import inso from '../image/fig_inso.png'
import noeat from '../image/fig_noeat.png'
import qui from '../image/fig_qui.png'
import sad from '../image/fig_sad.png'
import tor from '../image/fig_tor.png'

const Data =()=> {
    const [results, setResults] = useState([])
   
    const renderText=()=>{
        axios
        .get("api/post/1/showmodels/")
        .then(res => 
            setResults(res)
            )
        .catch(err => console.log(err))
    
    }

    useEffect(()=>{
        renderText();
        // console.log(results.length)
    })

    return(
            <div>
            <Grid centered>
                <Grid.Row centered/>
                <Grid.Row centered>
                    <Grid.Column>
                        <Progress percent={97.21} active>
                            학습률 60%
                        </Progress>
                    </Grid.Column>
                    
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {alone}
                        header='#1. 우울증별 외로움 정도'
                        meta='외롭다고 느끼는가?'
                        description='근 일주일간 세상에 홀로 있는 듯한 외로움을 느꼈다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {anxi}
                        header='#2. 우울증별 집중불안 정도'
                        meta='쉽게 집중하지 못하고 있나?'
                        description='근 일주일간 어떤 일을 하든 정신을 집중하기가 힘들었다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {bother}
                        header='#3. 우울증별 귀찮음 정도'
                        meta='요즘 귀찮나?'
                        description='근 일주일간 평소에는 아무렇지도 않던 일들이 귀찮게 느껴졌다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {capa}
                        header='#4. 우울증별 자기능력판단 정도'
                        meta='나는 능력이 있을까?'
                        description='근 일주일간 다른 사람만큼 자신이 능력 있다고 느꼈다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {cold}
                        header='#5. 우울증별 타인 생각 정도'
                        meta='사람들이 나를 차갑게 대하나?'
                        description='근 일주일간 사람들이 나를 차갑게 대하는 것 같았다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {cry}
                        header='#6. 우울증별 울음 정도'
                        meta='갑자기 울어버렸다?'
                        description='근 일주일간 갑자기 울음이 나왔다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {depr}
                        header='#7. 우울증별 우울 정도'
                        meta='우울한가?'
                        description='근 일주일간 우울했다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {fail}
                        header='#8. 우울증별 실패감 정도'
                        meta='내 인생은 실패?'
                        description='근 일주일간 내 인생은 실패작이라는 생각이 들었다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {fear}
                        header='#9. 우울증별 두려움 정도'
                        meta='두려움..?'
                        description='근 일주일간 두려움을 느꼈다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {fun}
                        header='#10. 우울증별 즐거움 정도'
                        meta='생활의 즐거움!'
                        description='근 일주일간 생활이 즐거웠다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {glo}
                        header='#11. 우울증별 울적한 정도'
                        meta='울적한가?'
                        description='근 일주일간 가족이나 친구가 도와주더라도 울적한 기분을 떨칠 수 없었다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {hap}
                        header='#12. 우울증별 행복한 정도'
                        meta='행복!'
                        description='근 일주일간 행복했다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {hard}
                        header='#13. 우울증별 힘듬 정도'
                        meta='모든 일이 힘들다?'
                        description='근 일주일간 하늘 일마다 힘들게 느껴졌다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {hate}
                        header='#14. 우울증별 타인반응 정도'
                        meta='사람들이 나를 싫어하나?'
                        description='근 일주일간 사람들이 나를 싫어하는 것 같았다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {hope}
                        header='#15. 우울증별 희망감 정도'
                        meta='내 미래는 희망적'
                        description='근 일주일간 미래에 대해 희망적이라고 느꼈다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {inso}
                        header='#16. 우울증별 불면 정도'
                        meta='잠을 설쳤나?'
                        description='근 일주일간 잠을 설쳤다. 잠을 잘 이루지 못했다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {noeat}
                        header='#17. 우울증별 식욕 정도'
                        meta='잘 먹지 못했나?'
                        description='근 일주일 간 음식을 먹고 싶지 않았다. 입맛이 없었다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {qui}
                        header='#18. 우울증별 말수 정도'
                        meta='내 말수가 줄었나?'
                        description='근 일주일간 평소보다 말을 적게 했다. 말수가 줄었다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {sad}
                        header='#19. 우울증별 슬픔 정도'
                        meta='얼마나 슬픔을 느꼈나?'
                        description='근 일주일간 슬픔을 느꼈다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>
                <Grid.Row centered>
                    <Grid.Column>
                        <Card
                        centered
                        image= {tor}
                        header='#20. 우울증별 의욕 정도'
                        meta='시작할 기운이 없었나?'
                        description='근 일주일간 도무지 무엇을 시작할 기운이 나지 않았다.'                 
                        />
                    </Grid.Column>          
                </Grid.Row>



            </Grid>
            </div>
    );
}

export default Data;