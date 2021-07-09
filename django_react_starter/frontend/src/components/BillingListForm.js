import React, { Component } from "react";

export class BillingListForm extends Component {
  state = {
    disabled: false,
    disabled2: false,
    buttonactivated: false,
  };

  // first function used to check if 'Export to Zip' needs to be disabled
  handle_customerChange = (e) => {
    if (e.target.value !== "All") {
      this.setState({
        disabled: true,
      });
    } else {
      this.setState({
        disabled: false,
      });
    }
  };

  // second function used to check if 'Export to Zip' needs to be disabled
  handle_paymentChange = (f) => {
    this.props.setButton("inactive");
    this.props.setType(f.target.value);
    if (f.target.value === "Mandate") {
      this.setState({
        disabled2: true,
      });
    } else {
      this.setState({
        disabled2: false,
      });
    }
  };

  // triggered when 'Get Billing List' is clicked
  // triggers the function imported form 'App.js'
  // (the functions activate setState)
  buttonfunc = () => {
    this.props.setButton("active");
    this.props.setCompany(this.state.selectedchoice);
    this.props.setRefNo(this.state.selectedref);
  };

  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      selectedchoice: -1,
      selectedref: -1,
    };
  }

  // function used to fetch API (Merchants table)
  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showmerchants";
    const response = await fetch(url);
    const data = await response.json();
    this.setState((prevState) => ({
      data1: data.data,
      selectedchoice: prevState.selectedchoice,
      selectedref: prevState.selectedref, // not passing the correct variable
    }));
  }

  // triggered when 'Select Company' is changed
  onTarget = (e) => {
    this.setState((prevState) => ({
      data1: prevState.data1,
      selectedchoice: e.target.value,
      selectedref: prevState.selectedref, // not passing the correct variable
    }));
  };

  render() {
    return (
      <div className="card card-body mt-4 mb-4">
        <label>Customer</label>
        <form>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.onTarget}
          >
            <option value={-1}>Select Customer</option>
            <option value={"All"}>All</option>
            {/* mapping function that renders all the company names */}
            {this.state.data1.map((x, y) => (
              <option value={x.id} key={y}>
                {x.company_name}
              </option>
            ))}
          </select>
          <div className="form-group">
            <label style={{ margin: "8px 0px 0px" }}>From</label>
            <input className="form-control" type="date" />
          </div>

          <div className="form-group">
            <label>To</label>
            <input className="form-control" type="date" />
          </div>
          <label>Type</label>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.handle_paymentChange}
          >
            <option defaultValue>Select Type</option>
            <option value="Mandate">Mandate</option>
            <option value="Instant Pay (Bank)">Instant Pay (Bank)</option>
            <option value="Instant Pay (Card)">Instant Pay (Card)</option>
            <option value="Successful Pay (Bank)">Successful Pay (Bank)</option>
            <option value="Successful Pay (Card)">Successful Pay (Card)</option>
          </select>
          <div className="d-grid">
            <button
              type="button"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
              onClick={this.buttonfunc}
            >
              Get Billing List
              {/* not completed */}
            </button>
          </div>

          <div className="btn-group d-md-flex mx-auto" role="toolbar">
            <button
              type="button"
              className="btn btn-outline-primary mr-2"
              style={{ minWidth: "205.5px" }}
              disabled={this.state.disabled || this.state.disabled2}
            >
              {/* has no functionality */}
              Export to Zip
            </button>
            <button
              type="button"
              className="btn btn-outline-primary"
              style={{ minWidth: "205.5px" }}
            >
              {/* has no functionality */}
              Export to Excel
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default BillingListForm;

// to do:
// 1. finish off the "mandate" type with each company; the columns 'company name', 'customer' and 'value' have not been finished
// 2. finish off the other types "instant pay" and "successful pay"
// 3. add functionalities to "export to zip" and "export to excel"
// 4. filter resultstable.js with the date
// 5. fix bug where when you select instant pay it crashes
// 6. fix the 'selectedref' state
// 7. the 'export to zip' button should be disabled when a customer (==! All) is chosen
// 8. 'merchant_id = all' doesnt work
// 9. 'invoiceform.js' is being pushed down after table is generated
// 10. loading status (or any thing to represent loading) while API is being fetched and files are being downloaded/formed from export buttons
