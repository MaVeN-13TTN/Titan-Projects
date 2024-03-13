// Roadmap data
const roadmap = [
  {
    month: 'Month 1 (Beginner Level)',
    topics: ['Python Fundamentals', 'Web Frameworks', 'Version Control'],
    subTopics: [
      'Syntax, data types, control flow',
      'Object-oriented programming (OOP)',
      'Functions, modules, and packages',
      'Introduction to Django',
      'Building simple CRUD applications with Django',
      'Git fundamentals',
      'Branching, merging, and collaboration on GitHub'
    ]
  },
  {
    month: 'Month 2 (Beginner/Intermediate Level)',
    topics: ['Web Frameworks', 'Databases'],
    subTopics: [
      'Advanced Django concepts (middleware, templates, ORM)',
      'Introduction to Flask',
      'Building simple CRUD applications with Flask',
      'SQL fundamentals',
      'Relational databases (PostgreSQL)',
      'Data modeling and schema design'
    ]
  },
  {
    month: 'Month 3 (Intermediate Level)',
    topics: ['API Development', 'API Security', 'Testing'],
    subTopics: [
      'RESTful API design principles',
      'Building RESTful APIs with Django REST Framework or Flask-RESTful',
      'Authentication and authorization (JWT, OAuth)',
      'OWASP API Security best practices',
      'Token-based authentication',
      'CORS and CSRF protection',
      'Unit testing in Python',
      'Test-driven development (TDD)'
    ]
  },
  {
    month: 'Month 4 (Intermediate Level)',
    topics: ['Software Design and Architecture', 'NoSQL Databases', 'Caching'],
    subTopics: [
      'Design patterns (MVC, Singleton, Factory)',
      'Architectural styles (microservices, monolithic)',
      'Designing scalable and maintainable systems',
      'MongoDB',
      'Data modeling for NoSQL databases',
      'Redis',
      'Caching strategies for performance optimization'
    ]
  },
  {
    month: 'Month 5 (Advanced Level)',
    topics: ['Cloud Services', 'Containerization', 'Message Brokers', 'Web Servers'],
    subTopics: [
      'AWS services (EC2, S3, Lambda)',
      'Firebase for real-time data synchronization',
      'Docker basics',
      'Container orchestration with Kubernetes',
      'RabbitMQ',
      'Pub-sub architecture and use cases',
      'NGINX for reverse proxy and load balancing'
    ]
  },
  {
    month: 'Month 6 (Advanced Level)',
    topics: ['GraphQL', 'Advanced Topics', 'Portfolio and Interview Preparation'],
    subTopics: [
      'Introduction to GraphQL',
      'Building GraphQL APIs',
      'Advantages over RESTful APIs',
      'Async programming and event-driven architecture',
      'WebSockets and real-time communication',
      'Serverless computing (AWS Lambda, Google Cloud Functions)',
      'Authentication mechanisms (OAuth, OpenID Connect)',
      'Build and deploy a full-fledged backend project',
      'Prepare a portfolio showcasing your projects',
      'Practice coding challenges and system design problems',
      'Prepare for behavioral and technical interviews'
    ]
  }
];

const tableBody = document.querySelector('#roadmapTable tbody');
const progressBar = document.querySelector('.progress-bar div');
let totalSubTopics = 0;
let completedSubTopics = 0;

// Load completed sub-topics count from localStorage on page load
for (let i = 0; i < localStorage.length; i++) {
  const key = localStorage.key(i);
  if (key.startsWith('subTopic-') && localStorage.getItem(key) === 'true') {
    completedSubTopics++;
  }
}

roadmap.forEach(month => {
  const row = document.createElement('tr');

  const monthCell = document.createElement('td');
  monthCell.textContent = month.month;
  row.appendChild(monthCell);

  const topicsCell = document.createElement('td');
  topicsCell.textContent = month.topics.join(', ');
  row.appendChild(topicsCell);

  const subTopicsCell = document.createElement('td');
  const subTopicsList = document.createElement('ul');
  month.subTopics.forEach(subTopic => {
    const subTopicItem = document.createElement('li');
    const subTopicCheckbox = document.createElement('input');
    subTopicCheckbox.type = 'checkbox';
    subTopicCheckbox.id = `subTopic-${totalSubTopics}`;
    subTopicCheckbox.addEventListener('change', updateProgressBar);

    // Check if the sub-topic is completed and update completedSubTopics count
    if (localStorage.getItem(`subTopic-${totalSubTopics}`) === 'true') {
      subTopicCheckbox.checked = true;
      subTopicItem.classList.add('completed');
      completedSubTopics++;
    }

    const subTopicLabel = document.createElement('label');
    subTopicLabel.htmlFor = `subTopic-${totalSubTopics}`;
    subTopicLabel.textContent = subTopic;

    subTopicItem.appendChild(subTopicCheckbox);
    subTopicItem.appendChild(subTopicLabel);
    subTopicsList.appendChild(subTopicItem);
    totalSubTopics++;
  });
  subTopicsCell.appendChild(subTopicsList);
  row.appendChild(subTopicsCell);

  tableBody.appendChild(row);
});

// Update the progress bar with the initial completed sub-topics count
updateProgressBar();

function updateProgressBar() {
    const completedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    completedSubTopics = completedCheckboxes.length;
  
    // Update localStorage for all checkboxes
    document.querySelectorAll('input[type="checkbox"]').forEach((checkbox, index) => {
      localStorage.setItem(`subTopic-${index}`, checkbox.checked);
    });
  
    const progress = (completedSubTopics / totalSubTopics) * 100;
    progressBar.style.width = `${progress}%`;
    progressBar.textContent = `${progress.toFixed(2)}%`;
  }
  