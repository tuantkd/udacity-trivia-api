import React, { Component } from 'react';
import $ from 'jquery';
import '../stylesheets/FormView.css';

class FormView extends Component {
  constructor(props) {
    super();
    this.state = {
      question: '',
      answer: '',
      difficulty: 1,
      category: 1,
      categories: {},
      validation: {}
    };
  }
  
  componentDidMount() {
    $.ajax({
      url: `/get-categories`,
      type: 'GET',
      success: (result) => {
        this.setState({ categories: result.categories });
        return;
      },
      error: (error) => {
        alert('Unable to load categories. Please try your request again');
        return;
      },
    });
  }

  submitQuestion = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/create-questions', //TODO: update request URL
      type: 'POST',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        question: this.state.question,
        answer: this.state.answer,
        difficulty: this.state.difficulty,
        category: this.state.category,
      }),
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      success: (result) => {
        if (result && result.validate.length > 0) {
          $("#messages-sucess").hide();
          $("#messages-validate").show();
          $("#messages-validate ul").empty();
          for (const value of result.validate) {
            $("#messages-validate ul").append("<li>" + value + "</li>");
          }
        } else {
          $("#messages-validate").hide();
          $("#messages-sucess").empty();
          $("#messages-sucess").show();
          $("#messages-sucess").append("<p>" + result.response + "</p>");
          document.getElementById('add-question-form').reset();
          // eslint-disable-next-line react/no-direct-mutation-state
          this.state.question = '';
          // eslint-disable-next-line react/no-direct-mutation-state
          this.state.answer = '';
        }
        return;
      },
      error: (error) => {
        alert('Unable to add question. Please try your request again');
        return;
      },
    });
  };

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };

  render() {
    return (
      <div id='add-form'>
        <h2>Add a New Trivia Question</h2>
        <div id="messages-validate"><ul></ul></div>
        <div id='messages-sucess'></div>

        <form className='form-view' id='add-question-form' onSubmit={this.submitQuestion}>
          <div className="input-group">
            <label>Question</label>
            <textarea name='question' onChange={this.handleChange} placeholder="Enter question" rows="3"></textarea>
          </div>
          
          <div className="input-group">
            <label>Answer</label>
            <input type='text' name='answer' onChange={this.handleChange} placeholder="Enter answer"/>
          </div>
          
          <div className="input-group">
            <label>Difficulty</label>
            <div className="select-dropdown">
              <select name='difficulty' onChange={this.handleChange}>
                <option value='1'>Difficulty 1</option>
                <option value='2'>Difficulty 2</option>
                <option value='3'>Difficulty 3</option>
                <option value='4'>Difficulty 4</option>
                <option value='5'>Difficulty 5</option>
              </select>
            </div>
          </div>

          <div className="input-group">
            <label>Category</label>
            <div className="select-dropdown">
              <select name='category' onChange={this.handleChange}>
                {Object.keys(this.state.categories).map((id) => {
                  return (<option key={id} value={this.state.categories[id].id}>{this.state.categories[id].type}</option>);
                })}
              </select>
            </div>
          </div>

          <div className="input-group">
            <label></label>
            <input id='btn-submit-form' type='submit' className='btn-submit-form' value='Submit' />
          </div>
        </form>
      </div>
    );
  }
}

export default FormView;
