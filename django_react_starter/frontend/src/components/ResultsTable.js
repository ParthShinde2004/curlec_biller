import React, { Component } from "react";

export class ResultsTable extends Component {
  //function for rendering
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
              {/* {{ funnctionName() }} later for when we progrma the function */}
              <tr>
                <th scope="row">1</th>
                <td>Company 1</td>
                <td>0000</td>
                <td>random date</td>
                <td>0000</td>
                <td>John Doe</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td>Company 2</td>
                <td>1111</td>
                <td>random date</td>
                <td>1111</td>
                <td>Song Li</td>
                <td>RM test</td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td>Company 3</td>
                <td>2222</td>
                <td>random date</td>
                <td>2222</td>
                <td>Mary Jane</td>
                <td>RM test</td>
              </tr>
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

export default ResultsTable;

// use functions (inside the component) to generate all the rows from backend
