import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor () {
    super()

    this.handleClick = this.handleClick.bind(this)
  }

  handleClick () {
  let url = "http://127.0.0.1:5000/"
  let xhr = new XMLHttpRequest()
  xhr.open("GET", url, false)
  xhr.send()
  setTimeout(() => {
  }, 100)
  let data = JSON.parse(xhr.responseText)
  const elem = document.getElementById("main1")
  function display(element){
  let title = element.title
  elem.insertAdjacentHTML("beforeend", "<button>" + title + "</button><input class='edit' type='button' value='Edit'><input class='delete' type='button' value='Delete'><br /><br />")
  }
  data.forEach(display)
  }

  render () {
    return (
      <div>
      <div className='button__container'>
        <button className='button' onClick={this.handleClick}>
          Click Me
        </button>
      </div>
      <div id="main1">
          <div><b>Main menu</b></div>
          <button id="button">Home</button>
          <br />
          <br />
      </div>
      </div>
    )
  }
}

export default App;
