import Button from "./Button";
import styles from "./App.module.css";
import { useEffect, useState } from "react";

function Hello() {
  // function byeFn() {
  //   console.log("'bye :(");
  // }
  // function hiFn() {
  //   console.log("hi :)");
  //   return byeFn;
  // }
  useEffect(() => {
    console.log("hi :)");
    return () => console.log("bye :(");
  }, []);
  useEffect(function() {
    console.log("hi :)");
    return function() {
      console.log("bye :(");
    }
  }, []);
  return <h1>Hello</h1>;
}

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");
  const [showing, setShowing] = useState(false);
  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  const onClick2 = () => setShowing((prev) => !prev);
  console.log("i run all the time");
  useEffect(() => {
    // console.log("CALL THE API...");
    console.log("I run only once.");
  }, []);
  useEffect(() => {
    // if (keyword !== "" && keyword.length > 5) {
    //   console.log("SEARCH FOR", keyword);
    // }
      console.log("I run when 'keyword' changes.");
  }, [keyword]);
  useEffect(() => {
    console.log("I run when 'counter' changes.");
  }, [counter]);
  useEffect(() => {
    console.log("I run when keyword & counter change.");
  }, [counter]);
  return (
    <div>
      <input 
        value={keyword}
        onChange={onChange} 
        type="text" 
        placeholder="Search here..." 
      />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
      {showing ? <Hello /> : null}
      <button onClick={onClick2}>{showing ? "Hide" : "Show"}</button>
    </div>
  );
}

export default App;