import React, { Component } from 'react';
import '../stylesheets/Search.css';

class Search extends Component {
  state = {
    query: '',
  };

  getInfo = (event) => {
    event.preventDefault();
    this.props.submitSearch(this.state.query);
  };

  handleInputChange = () => {
    this.setState({
      query: this.search.value,
    });
  };

  render() {
    return (
      <form onSubmit={this.getInfo}>
        <div className="form-search">
          <div className="input-text">
            <input type='text' placeholder='Search questions...' 
            ref={(input) => (this.search = input)} onChange={this.handleInputChange}/>
          </div>
          <div className="btn-submit">
            <input type='submit' value='Submit' className='btn'/>
          </div>
        </div>
      </form>
    );
  }
}

export default Search;
