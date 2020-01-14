import React, {useState} from 'react'
import { Form, Grid, Divider, Message, Segment } from 'semantic-ui-react'


const Reserve=()=>{
    const options = [
        { key: 'm', text: '다이어리 공개', value: 'open' },
        { key: 'f', text: '다이어리 비공개', value: 'close' },
      ]
      const options2 = [
        { key: '1', text: '강남구 신나라 센터', value: '1' },
        { key: '2', text: '유성구 행복 센터', value: '2' },
        { key: '3', text: '서초구 건강 센터', value: '3' },
        { key: '4', text: '유성구 심리 센터', value: '4' },
        { key: '5', text: '강남구 ㅁ 센터', value: '5' },
        { key: '6', text: '강남구 ㅂ 센터', value: '6' },

    ]

    const [value, setValue] = useState('');
    const handleChange = (e, { value }) => setValue(value)
    const [todata, setTodata] = useState(false);
    
    return(
        <div>
            <Grid>
                <Grid.Row />
            </Grid>
            <Grid columns='equal'>
            <Grid.Column />
            <Grid.Column width={13}>
            <Form>
            <Form.Group widths='equal'>
                <Form.Input fluid label='성명' placeholder='성명' />
                <Form.Input fluid label='별칭' placeholder='별칭 기입시 별칭으로 안내해드립니다.' />
            </Form.Group>
            <Form.Select
                    fluid
                    label='병원'
                    options={options2}
                    placeholder='병원 시설'
                />

            <Form.Select
                    fluid
                    label='다이어리 공개 여부'
                    options={options}
                    placeholder='의사에게 다이어리 공개 여부'
                />
                <Form.Group inline>
                <label>병원 경험 여부</label>
                <Form.Radio
                    label='yes'
                    value='yes'
                    checked={value === 'yes'}
                    onChange={handleChange}
                />
                <Form.Radio
                    label='no'
                    value='no'
                    checked={value === 'no'}
                    onChange={handleChange}
                />

                </Form.Group>
                <Form.TextArea label='기타' placeholder='기타 추가 문의 사항을 적으세요' />
                <Form.Checkbox label='추가 내용이 있다면 체크하세요' value='todata' onClick={()=>setTodata(!todata)}/>
                {todata == true ? 
                <Segment secondary>
                    <Form.Group widths='equal'>
                    <Form.Input fluid label='성명' placeholder='성명' />
                    <Form.Input fluid label='별칭' placeholder='별칭 기입시 별칭으로 안내해드립니다.' />
                    </Form.Group>
                    <Form.Select
                            fluid
                            label='병원'
                            options={options2}
                            placeholder='병원 시설'
                        />

                    <Form.Select
                            fluid
                            label='다이어리 공개 여부'
                            options={options}
                            placeholder='의사에게 다이어리 공개 여부'
                        />
                <Form.Group inline>
                    <label>병원 경험 여부</label>
                    <Form.Radio
                        label='yes'
                        value='yes'
                        checked={value === 'yes'}
                        onChange={handleChange}
                    />
                    <Form.Radio
                        label='no'
                        value='no'
                        checked={value === 'no'}
                        onChange={handleChange}
                    />
                </Form.Group>
                </Segment>   
                : ""}
                <Form.Button color='orange'>Submit</Form.Button>
            </Form>
            </Grid.Column>
            <Grid.Column/>
        </Grid>

        </div>
 
    )
}

export default Reserve