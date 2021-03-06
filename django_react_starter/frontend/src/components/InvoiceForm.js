import React, { Component } from "react";

export class InvoiceForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
    };
  }

  // calls API for 'Merchants' table
  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showmerchants";
    const response = await fetch(url);
    const data = await response.json();
    this.setState((prevState) => ({
      data1: data.data,
    }));
  }

  render() {
    return (
      //buttons had no functionallity
      <div className="card card-body mt-4 mb-4">
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>From</label>
            <input className="form-control" type="date" name="name" />
          </div>

          <div className="form-group">
            <label>To</label>
            <input className="form-control" type="date" name="name" />
          </div>
          <label>Is Live</label>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Yes</option>
            <option value="1">No</option>
          </select>
          <a></a>
          <div className="form-group">
            <button
              type="submit"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
            >
              Generate Invoice
            </button>
            <div className="btn-group d-md-flex mx-auto" role="toolbar">
              <button
                type="button"
                className="btn btn-outline-primary mr-2"
                style={{ minWidth: "205.5px" }}
              >
                Live Merchants
              </button>
              <button
                type="button"
                className="btn btn-outline-primary"
                style={{ minWidth: "205.5px" }}
              >
                Non-Live Merchants
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

export default InvoiceForm;

// to do:
// 1. the date 'from' and 'to' has no functionalities; so add functions [x]
// 2. 'Is Live' is not working [x]
// 3. add functionalities to 'Live Merchants' and 'Non-Live Merchants' buttons [x]
// 4. add functionalities to 'Generate Invoice' button [x]
// 5. loading status (or any thing to represent loading) while API is being fetched and files are being downloaded/formed from buttons [x]
