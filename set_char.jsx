import React from "react";
import ReactDOM from "react-dom";

class App extends React.Component {
 constructor() {
  super();
  this.state = {
   character: "Plumber",
   clothes: "Overalls",
  };
 }

 setCharacter = () => {
  const c = this.state.character;
  if (c == "Plumber") {
   this.setState({
    character: "Marsupial",
   });
  } else {
   this.setState({
    character: "Plumber",
   });
  }
 };

 setClothes = () => {
  const c = this.state.clothes;
  if (c == "Overalls") {
   this.setState({
    clothes: "Shorts",
   });
  } else {
   this.setState({
    clothes: "Overalls",
   });
  }
 };

 render() {
  return (
   <div>
    <h1>Create your Character</h1>
    <h2>Your current character is:</h2>
    <h3>{this.state.character}</h3>
    <p>
     in <strong>{this.state.clothes}</strong>
    </p>

    <button onClick={this.setCharacter}>Switch Character</button>
    <button onClick={this.setClothes}>Switch Clothes</button>
   </div>
  );
 }
}

ReactDOM.render(<App />, document.getElementById("root"));
