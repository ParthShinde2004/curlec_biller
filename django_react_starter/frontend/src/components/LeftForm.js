import React, { Component } from "react";

export class LeftForm extends Component {
  state = {
    name: "",
    email: "",
    message: "",
  };
  render() {
    const { name, message, email } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Customer</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>From</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>To</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>Type</label>
            <textarea
              className="form-control"
              type="text"
              name="message"
              onChange={this.onChange}
              value={message}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Get Mailing List
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default LeftForm;
