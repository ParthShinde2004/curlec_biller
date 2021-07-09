import React, { Component } from "react";

export class ResultsTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
    };
  }
  async componentDidUpdate(prevProps, prevState) {
    if (this.props.selectedCompany !== prevProps.selectedCompany) {
      const url = `http://127.0.0.1:8000/api/showmandates?merchant_id=${this.props.selectedCompany}`;
      const url1 = `http://127.0.0.1:8000/api/showtransactions?id=${this.props.selectedCompany}`;
      const response = await fetch(url);
      const response1 = await fetch(url1);
      const data = await response.json();
      const data2 = await response1.json();
      this.setState((prevState) => ({
        data1: data.data,
        data3: data2.data,
      }));
    }
  }

  onTarget = (e) => {
    this.setState((prevState) => ({
      data1: prevState.data1,
      data3: prevState.data3,
    }));
  };

  renderrow = (x, y) => {
    if (x == null) {
      return false;
    }
    return (
      <tr>
        <td>{y + 1}</td>
        <td>company</td>
        <td>{x.merchant_id}</td>
        <td>{x.date_created}</td>
        <td>{x.reference_number}</td>
        <td>customer</td>
        <td>value</td>
      </tr>
    );
  };

  renderrow1 = (z, w) => {
    if (z == null) {
      return false;
    }
    return (
      <tr>
        <td>{w + 1}</td>
        <td>Company</td>
        <td>{z.merchant_id}</td>
        <td>{z.date_created}</td>
        <td>Order Number</td>
        <td>Value</td>
      </tr>
    );
  };

  //function for rendering; map; html <tr>; hard code a few rows first
  render() {
    if (this.props.buttonStatus === "inactive") return false;
    return (
      <div className="table-responsive">
        {this.props.transactionType == "Mandate" && (
          <table className="table" align="right">
            <thead>
              <tr>
                <th scope="col">No</th>
                <th scope="col">Company Name</th>
                <th scope="col">Merchant ID</th>
                <th scope="col">Date</th>
                <th scope="col">Reference</th>
                <th scope="col">Customer</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
            <tbody>
              {this.state.data1.length != 0 && (
                <>{this.state.data1.map((x, y) => this.renderrow(x, y))}</>
              )}
            </tbody>
          </table>
        )}
        {this.props.transactionType == "Instant Pay (Bank)" && (
          <table className="table" align="right">
            <thead>
              <tr>
                <th scope="col">No</th>
                <th scope="col">Company Name</th>
                <th scope="col">Merchant ID</th>
                <th scope="col">Date</th>
                <th scope="col">Order Number</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
            <tbody>
              {this.state.data3.length != 0 && (
                <>{this.state.data3.map((w, z) => this.renderrow1(w, z))}</>
              )}
            </tbody>
          </table>
        )}
        {this.props.transactionType == "Instant Pay (Card)" && (
          <table className="table" align="right">
            <thead>
              <tr>
                <th scope="col">No</th>
                <th scope="col">Company Name</th>
                <th scope="col">Merchant ID</th>
                <th scope="col">Date</th>
                <th scope="col">Order Number</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
          </table>
        )}
        {this.props.transactionType == "Successful Pay (Bank)" && (
          <table className="table" align="right">
            <thead>
              <tr>
                <th scope="col">No</th>
                <th scope="col">Company Name</th>
                <th scope="col">Merchant ID</th>
                <th scope="col">Date</th>
                <th scope="col">Reference Number</th>
                <th scope="col">Customer</th>
                <th scope="col">Credit Card</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
          </table>
        )}
        {this.props.transactionType == "Successful Pay (Card)" && (
          <table className="table" align="right">
            <thead>
              <tr>
                <th scope="col">No</th>
                <th scope="col">Company Name</th>
                <th scope="col">Merchant ID</th>
                <th scope="col">Date</th>
                <th scope="col">Reference Number</th>
                <th scope="col">Customer</th>
                <th scope="col">Credit Card</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
          </table>
        )}
      </div>
    );
  }
}

export default ResultsTable;
