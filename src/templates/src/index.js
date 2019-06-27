import React, { Component } from "react";
import ReactDOM from "react-dom";

class App extends Component {
    render() {
        return(
            <div>
            <h1>Hello From ReactJS!</h1>
            <p>Its kinda hard using flask at the beginning</p>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById("root"))