import React from 'react'
import { Grid, Image, Header, Icon } from 'semantic-ui-react'
import mangos from '../image/mango.png' //이미지 import의 경우, src 폴더를 벗어나면 불가

const divmargin = {
    margin : 6
}

const Headers = ()=> {
    return(
        <div>

            <Grid columns='equal' style = {divmargin}>
                <Grid.Row only='computer'>
                    <Grid.Column width={10}>                     
                            <Header as='h3' color='orange'textAlign="left">
                                <Image src={mangos} size='mini' verticalAlign="middle"/>
                                APPLEMANGO
                            </Header>
                    </Grid.Column>
                    <Grid.Column textAlign='right'>
                        <Icon name='lock' size='large' corner='top right'/>
                    </Grid.Column>
                </Grid.Row>

                <Grid.Row only='tablet mobile'>
                    <Grid.Column/>
                    <Grid.Column width={10}>                     
                            <Header as='h4' color='orange'textAlign="center">
                                <Image src={mangos} size='mini' verticalAlign="middle"/>
                                APPLEMANGO
                            </Header>
                    </Grid.Column>
                    <Grid.Column textAlign='right'>
                        <Icon name='lock' size='large' corner='top right'/>
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </div>
    );

}

export default Headers;


