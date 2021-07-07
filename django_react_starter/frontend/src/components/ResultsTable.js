import React, { Component } from "react";

export class ResultsTable extends Component {
  constructor(props) {
    super(props);
    this.getHeader = this.getHeader.bind(this);
    this.getRowsData = this.getRowsData.bind(this);
    this.getKeys = this.getKeys.bind(this);
  }

  getKeys = () => {
    console.log(data.data);
    return Object.keys(this.props.data.data[0]);
  };

  getRowsData = () => {};

  getHeader = () => {
    let keys = this.getKeys();
    return keys.map((key, index) => {
      return <th key={key}>{key.toUpperCase()}</th>;
    });
  };

  //   this.state = {
  //     data1: [],
  //     selectedchoice: -1,
  //   };
  // }
  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showmerchants";
    const response = await fetch(url);
    const data = await response.json();
    // this.setState((prevState) => ({
    //   data1: data.data,
    //   selectedchoice: prevState.selectedchoice,
    // }));
  }

  mandatetable = () => {
    const table1 = document.getElementById("mandatetable");

    for (let i = 0; i < data1.length; i++) {
      let row = `<tr>
                    <td>${i}</td>
                    <td>${data1[i].id}</td>
                </tr>`;
      table1.innerHTML += row;
    }
  };

  //function for rendering
  render() {
    if (this.props.buttonStatus === "inactive") return false;
    return (
      <div className="table-responsive">
        <table>
          <thead>
            <tr>{this.getHeader()}</tr>
          </thead>
          <tbody>{this.getRowsData()}</tbody>
        </table>
        {/* {this.props.transactionType == "Mandate" && (
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
            <tbody> */}
        {/* {{ funnctionName() }} later for when we progrma the function */}
        {/* <tr>
                <th scope="row">1</th>
                <td>Company 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>0000</td>
                <td>John Doe</td>
                <td>RM test</td>
              </tr>
            </tbody>
          </table>
        )} */}
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
