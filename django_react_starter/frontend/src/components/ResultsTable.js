import React, { Component } from "react";

export class ResultsTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      // selectedchoice: -1,
    };
  }
  async componentDidUpdate(prevProps, prevState) {
    if (this.props.selectedCompany !== prevProps.selectedCompany) {
      console.log("didupdate");
      const url = `http://127.0.0.1:8000/api/showmandates?merchant_id=${this.props.selectedCompany}`;
      const url1 = "http://127.0.0.1:8000/api/showtransactions";
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
      // selectedchoice: e.target.value,
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
        <td>{x.reference_number}</td>
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
              <tr>
                <th scope="row">1</th>
                <td>Company 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Company 2</td>
                <td>1111</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Company 3</td>
                <td>2222</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
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
            <tbody>
              {/* {{ funnctionName() }} later for when we progrma the function */}
              <tr>
                <th scope="row">1</th>
                <td>Company 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Company 2</td>
                <td>1111</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Company 3</td>
                <td>2222</td>
                <td>random date</td>
                <td>CSB-IP-xxxxx</td>
                <td>RM test</td>
              </tr>
            </tbody>
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
            <tbody>
              {/* {{ funnctionName() }} later for when we progrma the function */}
              <tr>
                <th scope="row">1</th>
                <td>Customer 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>0000</td>
                <td>John Doe</td>
                <td></td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Company 2</td>
                <td>1111</td>
                <td>random date</td>
                <td>1111</td>
                <td>Song Li</td>
                <td>True</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Company 3</td>
                <td>2222</td>
                <td>random date</td>
                <td>2222</td>
                <td>Mary Jane</td>
                <td></td>
                <td>RM test</td>
              </tr>
            </tbody>
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
            <tbody>
              {/* {{ funnctionName() }} later for when we progrma the function */}
              <tr>
                <th scope="row">1</th>
                <td>Customer 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>0000</td>
                <td>John Doe</td>
                <td>True</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Company 2</td>
                <td>1111</td>
                <td>random date</td>
                <td>1111</td>
                <td>Song Li</td>
                <td>True</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Company 3</td>
                <td>2222</td>
                <td>random date</td>
                <td>2222</td>
                <td>Mary Jane</td>
                <td>True</td>
                <td>RM test</td>
              </tr>
            </tbody>
          </table>
        )}
      </div>
    );
  }
}

const RenderRow = (props) => {
  return props.keys.map((key, index) => {
    return <td key={props.data[key]}>{props.data[key]}</td>;
  });
};

export default ResultsTable;

// use functions (inside the component) to generate all the rows from backend
