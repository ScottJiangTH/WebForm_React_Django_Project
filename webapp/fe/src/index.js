import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Section1 from './Section1';
import Section2 from './Section2';
import Section7 from './Section7';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <Section1 />
    <Section2 />
    <Section7 />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
