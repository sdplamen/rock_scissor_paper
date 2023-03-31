import React from "react";
import ReactDOM from "react-dom";

class App extends React.Component {
 constructor() {
  super();
  this.state = { 
   text: "",
   desc: "" 
  }
 }

 handleChange = (e) => {
  this.setState({
   text: e.target.value
  });
 }

 submitDesc = () => {
  const t = this.state.text;
  this.setState({
   text: "",
   desc: t
  })
 }

 render() {
  return (
   <div>
    <img src="https://mimo.app/i/salmon-dish.png" alt="Salmon" />
    <p>Enter a brief description of the image.</p>
    <input 
     type="text"
     name="desc"
     value={this.state.text}
     onChange={this.handleChange}
    />
    <button onClick={this.submitDesc}>
     Submit Description
    </button>
    <h5>Your Description:</h5>
    <p><i>{this.state.desc}</i></p>
   </div>
  );
 }
}

ReactDOM.render(
 <App />,
 document.getElementById("root")
);
