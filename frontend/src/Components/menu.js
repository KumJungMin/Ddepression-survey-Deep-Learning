import React, {setState, useState} from 'react'
import { Grid, Button, Header, Menu } from 'semantic-ui-react'
import Background from '../image/background.jpeg'
import { Link } from "react-router-dom";

const backImage = {
    backgroundImage: "url(" + Background + ")",
    backgroundRepeat : "no-repeat",
    backgroundSize : "cover"
    // backgroundImage: `url(${Background})`ES6 버전
}
const padding = {
    padding : 15
}
const fontcolor = {
    color : "#cc6600"
}



const Menus =()=> {
    const [activeItem, setActiveItem] = useState('')
    const handleItemClick = (e, { name }) => setActiveItem(name)

    return(
        <div>
            <Grid>
                <Grid.Row columns={5} style={backImage}>
                    <Grid.Column textAlign="right">
                         
                            {/* Profile */}
                            <Button circular icon='user' inverted/> 
                                <p style={fontcolor}>Profile
                                </p>
                        
                        {/* 라우트를 설정 할 때에는 Route 컴포넌트를 사용하고, 경로는 path 값으로 설정합니다. */}
                    </Grid.Column>
                    <Grid.Column textAlign="center">
                        <Button circular icon='address book' inverted/>
                        <p style={fontcolor}>Status</p>
                    </Grid.Column>
                    <Grid.Column textAlign="center">
                    <Link to="/diary">
                        <Button circular icon='book' inverted/>
                        <p style={fontcolor}>Diary</p>
                        </Link>
                    </Grid.Column>
                    <Grid.Column textAlign="center">
                    <Link to="/reserve">
                        <Button circular icon='plus' inverted/>
                        <p style={fontcolor}>Reserve</p>
                        </Link>
                    </Grid.Column>
                    <Grid.Column textAlign="center">
                    <Link to="/data">
                        <Button circular icon='chart bar' inverted/>
                        <p style={fontcolor}>Data</p>
                        </Link>
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </div>
    );
}
// yarn add react-router-dom
export default Menus;