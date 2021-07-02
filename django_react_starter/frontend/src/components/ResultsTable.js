import React, { Component } from "react";

export class ResultsTable extends Component {
  render() {
    return (
      // {{ var == "Mandate" &&
      <div className="table-responsive">
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
            <tr>
              <th scope="row">1</th>
              <td>Customer 1</td>
              <td>0000</td>
              <td>random date</td>
              <td>0000</td>
              <td>John Doe</td>
              <td>xxxx-xxxx-xxxx-xxxx</td>
              <td>RM test</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Company 2</td>
              <td>1111</td>
              <td>random date</td>
              <td>1111</td>
              <td>Song Li</td>
              <td>xxxx-xxxx-xxxx-xxxx</td>
              <td>RM test</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Company 3</td>
              <td>2222</td>
              <td>random date</td>
              <td>2222</td>
              <td>Mary Jane</td>
              <td>xxxx-xxxx-xxxx-xxxx</td>
              <td>RM test</td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}

export default ResultsTable;
