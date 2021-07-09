import React, { Component } from "react";
import { Modal, Button } from "react-bootstrap";

export class PopUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      selectedchoice: -1,
    };
  }

  // showcalculations API is fetched
  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showcalculations";
    const response = await fetch(url);
    const data = await response.json();
    this.setState((prevState) => ({
      data1: data.data,
      selectedchoice: prevState.selectedchoice,
    }));
  }

  // sets the selectedchoice state to the value of the dropdown
  onTarget = (e) => {
    this.setState((prevState) => ({
      data1: prevState.data1,
      selectedchoice: e.target.value,
    }));
  };

  render() {
    return (
      <Modal
        {...this.props}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header className="bg-primary">
          <Modal.Title id="contained-modal-title-vcenter" className="text-info">
            Calculation Rules Settings
          </Modal.Title>
          <button
            type="button"
            className="close"
            data-dismiss="modal"
            onClick={this.props.onHide}
          >
            <span aria-hidden="true" className="modal_button">
              &times;
            </span>
            <span className="sr-only">Close</span>
          </button>
        </Modal.Header>
        <Modal.Body>
          <h5>Customer</h5>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            //the state of selectedchoice stores the customer we clicked on
            onChange={this.onTarget}
          >
            {/* maps all the customers from the database */}
            <option value={-1}>Select Customer</option>
            {this.state.data1.map((x, y) => (
              <option value={y} key={y}>
                {x.company_name}
              </option>
            ))}
          </select>
          {/* Generates all the calculation data from the DB when it's chosen */}
          <h5>Calculation Rule - Credit Card:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_creditcard"
                ]}
            </a>
          </div>
          <h5>Calculation Rule - CASA:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_casa"
                ]}
            </a>
          </div>
          <h5>Calculation Rule - Instant Pay:</h5>
          <div className="input-group">
            <div>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_instant_pay"
                ]}
            </div>
          </div>
          <h5>Calculation Rule - Monthly Dashboard Fee:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_creditcard"
                ]}
            </a>
          </div>
          <h5>Calculation Rule - Monthly Credit Card Fee:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_credit_card_fee"
                ]}
            </a>
          </div>
          <h5>Calculation Rule - Monthly Minimum Fee:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_minimum_fee"
                ]}
            </a>
          </div>
          <h5>Calculation Rule - Mandate Fee:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_mandate_fee"
                ]}
            </a>
          </div>
          <h5>Discount Rate - Credit Card:</h5>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_cc_discount"
                ]}
            </a>
          </div>
          {/* Currently not working. Check to do list */}
          <h5>Is Live</h5>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Yes</option>
            <option value="1">No</option>
          </select>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={this.props.onHide}>Save</Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default PopUp;

// to do list:
// 1. aesthetics of the box (margin with each calculation rule)
// 2. make the calculation data editable
// 2. functionality of the save button; make sure to update back-end db when calculation data is changed
// 3. display the correct status for 'Is Live' (currently not working)
