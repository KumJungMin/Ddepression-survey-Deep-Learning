import { Header, Icon, Image, Grid, Button, Segment } from 'semantic-ui-react'
import React from 'react'
import Background from '../image/background.jpeg'

const margins = {
    margin : 6
}
const backImage = {
    backgroundImage: "url(" + Background + ")",
    backgroundRepeat : "no-repeat",
    backgroundSize : "cover"
    // backgroundImage: `url(${Background})`ES6 버전
}

const User = () => {
    return(
        <div>
            <Grid style={margins}/>
            <Grid>
                <Grid.Row only='computer' />

                <Grid.Row only='tablet mobile'>
                    <Header as='h4' icon textAlign='center'>
                        <Icon name='user outline' circular />
                        <Header.Content size='large'>USERNAME</Header.Content>
                        <Header.Subheader size='tiny'>
                            자기소개를 입력하시오 
                        </Header.Subheader>
                    </Header>
                </Grid.Row>

            </Grid>
      </div>
    );
}
   
  export default User