import React, { Component } from "react";

const students = [
  {
    id: 1,
    first_name: "David",
    family_name: "Zhang",
    date_of_birth: "2020/3/3",
    email_address: "zb.ramble@gmail.com",
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      studentList: students,
    };
  }

  // displayCompleted = (status) => {
  //   if (status) {
  //     return this.setState({ viewCompleted: true });
  //   }

  //   return this.setState({ viewCompleted: false });
  // };

  // renderTabList = () => {
  //   return (
  //     <div className="nav nav-tabs">
  //       <span
  //         className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
  //         onClick={() => this.displayCompleted(true)}
  //       >
  //         Complete
  //       </span>
  //       <span
  //         className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
  //         onClick={() => this.displayCompleted(false)}
  //       >
  //         Incomplete
  //       </span>
  //     </div>
  //   );
  // };

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.studentList;

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
          title={item.first_name}
        >
          {item.family_name}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  Add task
                </button>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;