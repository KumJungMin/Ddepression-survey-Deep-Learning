import React, {useState} from 'react'
import { Button, Form, Grid, Message, Rating, Divider, Header, TextArea, Checkbox } from 'semantic-ui-react'

const Diary = () => {


  const [checks, setChecks] = useState(false);

  return(
  <div>
    <Grid>
      <Grid.Row />
    </Grid>
    <Message
      attached
      header='감정 다이어리'
      content='매일매일 어땠는지, 내 감정 점수 평가와 함께 다이어리를 작성해보아요'
    />
    <Button.Group fluid>
      <Button color="yellow" onClick={()=>setChecks(false)}>리스트보기</Button>
      <Button.Or />
      <Button color="orange" onClick={()=>setChecks(true)}>등록하기</Button>
    </Button.Group>
    {checks == true ? 
      <Form className='attached fluid segment'>
      <Form.Group widths='equal'>
        <Form.Input
          fluid
          label='제목'
          placeholder='제목을 작성하시오'
          type='text'
        />
       
        <Form.Input
          fluid
          label='날짜'
          placeholder='0000.00.00'
        />
      </Form.Group>
      <Divider />
      <Header as='h5'>오늘 감정 점수는?</Header>
       <Rating icon='heart' defaultRating={1} maxRating={5} />
       <Divider />
           <TextArea placeholder='이야기를 적어 보아요' style={{ minHeight: 100 }} />

       <Divider />
      <Button color='orange'>내 감정 저장하기</Button>
    </Form>  : "ddd"
  
  }

  </div>)
}

export default Diary