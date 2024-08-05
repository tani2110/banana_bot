def prompt(user_input):
    import os
    import openai
    import hi
    # Now you can access your environment variables using os.getenv
    api_key = os.getenv('Ysk-GdmcQoSJjHjOte4Dgi5zT3BlbkFJaRMOwcg7mRplRQSKys8j')

    import datetime
    # Get the current date
    current_date = datetime.datetime.now().date()

    # Define the date after which the model should be set to "gpt-3.5-turbo"
    target_date = datetime.date(2024, 6, 12)

    # Set the model variable based on the current date
    llm_model = "gpt-4-0125-preview"

    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.chains import LLMChain

    llm = ChatOpenAI(temperature=0, model=llm_model, openai_api_key='MY-ENV')

    course_details="""




#     The semester started on 9th January 2024.
# These below dates are the holidays in the semester. No classes ha
# January 9 (T) Second Semester begins
# January 9 (T) Registration for all students
# January 10 (W) Practice School II begins
# January 10 (W) Class-work begins
# January 15 (M) Makar Sankranti (H)
# January 22 (M) Last day for substitution of courses
# January 25 (Th) Friday Timetable to be followed
# January 26 (F) Republic Day (H)
# February 1(Th) to 4(Su) Sports fest, ARENA
# February 8(Th) Monday Timetable to be followed
# March 8 (F) Maha Shivratri (H)
# March 11 (M) to March 16 (S) Mid Semester Exams
# March 19 (T) Last day for withdrawal from courses
# March 21 (Th) Last day of returning evaluated answer scripts of Mid-Semester grading
# March 25 (M) Holi (H)
# March 27 (W) Last day of Mid-Semester grading
# March 29 (F) Good Friday (H)
# March 29 (F) to 31 (Su) Cultural fest, PEARL, (Classwork Suspended)
# April 3rd(W) Monday Timetable to be followed
# April 9 (T) Ugadi (H)
# April 11 (Th) Id-ul-Fitr*(H)
# April 14 (Su) Ambedkar Jayanti (H)
# April 17 (W) Ram Navami (H)
# April 21 (Su) Mahavir Jayanti (H)
# April 22 (M) Registration for Practice School I
# April 27 (S) Last day of Pre-comprehensive marks display
# May 03 (F) Last day for class work
# May 06 (M) Comprehensive Examination begins
# May 20 (M) Comprehensive Examination ends
# May 20 (M) Second Semester ends
# May 23 (Th) Buddha Purnima (H)
# May 27 (M) Summer Vacation begins
# May 28 (T) Summer Term begins
# May 28 (T) Practice School I begins
# June 17 (M) Id-ul-Zuha (H)
# June 20 (Th) Practice School II ends
# July 23 (T) Practice School I ends
# July 23 (T) Summer Term ends
# July 23 (T) Summer Vacation ends

# Saturdays and Sundays are holidays.

    






# Group 1:
# Electrical Science(EEE F111):-
# Textbooks:-
# Fundamentals of Electrical Engineering Adapted by Naveen Gupta,
# Asian Edition, OUP Leonard S. Bobrow
# IC:-MITHUN MONDAL
# IC Room Number :- H-214
# IC Email:- mithun@hyderabad.bits-pilani.ac.in
# IC Phone:- 040 66303 564
# Room Number:-F103
# MidSem Exam:-15/03 - 2.00 - 3.30PM
# Compre Exam:-17/05 FN
# Course Plan:-

# Lect. No.
# Learning Objectives
# Topics to be covered
# Chapters  in Text Book 
# 1
# Introduction
# Introduction


# 2-5
# To study basic circuit elements and the laws; 
# Voltage and current sources, Independent and Dependent sources, 
# Resistors and Ohm’s law, inductors and capacitors and their integral relations ships.
# KCL, KVL; Current divider, Voltage divider rule, Instantaneous power
# 1.1 to 1.8  
# 6-9
# To study circuit analysis techniques and theorems.
# Mesh and Nodal Analysis,
# Thevenin’s and Norton’s Theorems
# Source transformation and Maximum Power Transfer Theorem,
# 2.1 to 2.4, 2.5
# 10
# To study circuit analysis techniques and theorems.
# Linearity and Superposition application in circuit analysis.
# 2.6
# 11-15
# Time Domain Analysis
# First order circuits and natural response; First order circuits and complete response.
# Second Order Circuits
# 3.1 to 3.5
# 16-20
# Alternating current circuits
# A.C. Voltage & Current, 
# Complex numbers, 
# Frequency and Time Domain analysis.
# 4.1-4.5 and 5.1
# 21-23
# Alternating current circuits
# Power and Power-factors, Poly-Phase circuits
# 4.6 to 4.7
# 24-27
# Magnetic Circuits
# Fundamentals of Electromagnetics.
# Series and parallel magnetic circuits.
# Laws of Electromagnetic induction.
# Principle of a Transformer, ideal operation with phasor diagram
# Losses calculation, rating, OC and SC tests.
# 13.1 to 13.7
# 28-32
# Electrical Machines 
# DC Motors and generators
# AC Motors and generators
# 15.1, 15.2 
# 33-35
# Digital Electronics
# Binary numbers, Binary Arithmetic, Digital logic circuits and Boolean algebra
# 12.1 to 12.4
# 36-38
# Basic Electronics
# Types of materials, classification of semiconductors, doping, introduction to semiconductor devices – diodes and transistors
# 6.1-6.8
# 39-42
# Bipolar Junction Transistors
# Basic operation of pnp and npn transistors, cutoff and saturation
# 7.1-7.3


# Course Description:
# The course covers various passive and active elements used in electrical networks, dependent and independent voltage and current sources (both DC and AC), analysis of DC and AC networks – KCL, KVL, network theorems, analysis and response of single order and second order circuits, polyphase circuits, magnetics, electromagnetic induction, transformers and basics of rotating electrical machines, basic electronic circuits using diodes and transistors, biasing and applications, operational amplifiers and introduction to digital electronics.
# Scope and objective of the Course: 
# Understanding physics of operation of electrical and electronic ciruits with various passive and active elements is required for all the engineering and science professionals. This course is designed to given the students of all engineering and science streams to give a primary exposure to basic electrical engineering. This is quite important for the students which will be useful for their career growth.
# The objective of the course is to obtain basic knowledge on:
# 		a. Electrical and Magnetic Circuits.
# 		b. Electrical machines.
# 	c. Semiconductor Diodes and BJTs ; Digital electronics.
# Evaluation Scheme:
# Component
# Duration
# Percentage weightage
# Maximum Marks
# Date & Time
# (Tentative)
# Remarks
# Daily interaction and assessment
# 5-10 min
# 10%
# 30 M
# Daily, during the lecture sessions
# OB
# Quizzes (2)
# 40 min
# 20%
# 2 X 30  =
# 60 M
# It will be announced a week before in the class 
# OB
# Mid-term exam 
# 90 min
# 30%
# 90M
# 15/03 - 2.00 - 3.30PM
# CB
# Comprehensive Examination
# 3 hours
# 40%
# 120M
# 17/05 FN
# CB






# Mechanical Oscillations and Waves(PHY F111):-
# Textbooks:-
# (i) by D. Kleppner and R. Kolenkow An Introduction to Mechanics Cambridge University Press, Second edition 2021
# IC:-PK Thiruvikraman
# IC Room No: A220  
# IC Email: thiru@hyderabad.bits-pilani.ac.in
# IC Phone: 040-66303508

# Room Number:-F102
# MidSem Exam:-12/03 - 2.00 - 3.30PM
# Compre Exam:-08/05 AN
# Course Plan:-

# Lecture Number
# Learning Objectives
# Topics to be covered
# Suggested Chapter/Section
# 1
# Introduction
# The Spirit of Newtonian Mechanics
# CLASS NOTE
# 2-3
# Vectors and Kinematics
# Velocity and Acceleration, Motion in Plane Polar Coordinates
# 1.7-1.11  (TB1)
# 4-8
# To understand the concept of Angular Momentum and to study rotation of a rigid body about a fixed axis
# Angular Momentum, Torque, Fixed axis rotation, Physical Pendulum
# 7.1-7.9 (TB1)
# 9-14
# Understand Central Force Motion
# Central force motion, Energy diagrams, planetary motion, Kepler’s laws
# 10.1-10.6 (TB1)
# 15-16
# Calculate frequency of small oscillations for arbitrary potentials
# Introduction and review of SHM, Energy diagrams, Small oscillations in a bound system
# 5.5-5.7, 11.1-11.2 (TB1)
# 17-18
# Damped harmonic oscillator
# Lightly damped, heavily damped, and critically damped oscillations, Q factor
# 11.3 (TB1)
# 19-20
# Forced harmonic oscillator
# Undamped forced oscillator, resonance, forced damped oscillator, Q factor
# 11.4-11.6 (TB1)
# 21-23
# To learn how vibrations can be combined to give more general vibrations leading to beats.
# Superposed vibrations in 1D, two superposed vibrations of equal and unequal frequencies, beats, Lissajous figures
# Chapter 2 – pages 19-39 (TB2)
# 24-25
# To analyze the behavior of undamped coupled harmonic oscillators. Define normal modes and describe how they may be combined.
# Coupled oscillators, normal modes, forced coupled oscillators
# Chapter 5 (TB2)
# Pages: 119-135
# 26-28
# To find the normal modes of coupled pendulums. To determine the   motion of coupled pendulums from their initial conditions. 
# Matrix method for finding normal mode frequencies, matrices, eigenvalues and eigenvectors
# Class notes
# 29-32
# To learn how to set up the wave equation. To learn how a normal mode of vibration of a stretched string is describable as a combination of two progressive waves. To find the total energy associated with one complete wavelength of a sinusoidal wave on a stretched string. 
# The free vibrations of stretched string, Progressive Waves, the energy in a mechanical wave, phase and group velocity
# Chapter 6 – TB2 (Pages: 161-170)
# Chapter 7 (Pages: 201-212) – TB2
# 33-34
# To distinguish between particle and wave/phase velocity.
# Superposition of waves, energy in mechanical wave
# Pages 213-215, 230-234, 237-242 (TB2)
# 35-40
# To describe interference from multiple sources. Study diffraction grating and diffraction by a single and double slit.
# Reflection of wave pulses, Interference from two and more than two sources, diffraction grating, diffraction by a single slit
# Chapter 8 (TB2)
# Pages: 253-259,267-274, 280-298


# Course Description: “Mechanics, Oscillations, and Waves” serves as a fundamental course in physics for science and engineering. This course, consisting of a series of lectures coupled with several demonstrations, provides a good, sound, working knowledge of the following topics: polar coordinates, angular momentum, central force motion, harmonic oscillator, coupled oscillations, waves and wave equation.

# Scope & Objective: Newtonian mechanics, the oldest branch of physics, is rather robust and possesses a very solid foundation. The phenomena of oscillations and waves have always been intriguing and are ubiquitous in the world around us. A course on “Mechanics, Oscillations, and Waves” is indispensable to understand other branches of science and engineering and serves as one of the stepping stones for scientific, engineering and medical research and development. The wide-ranging spectrum of subject matter of this course provides a foundation for advanced level physics courses. The objective of this course is to develop good physics problem-solving skills by building a deep conceptual understanding of the subject.
# Evaluation Scheme:
# S. No. 
# Evaluation Component 
# Duration 
# Weightage (%) 
# Date & Time 
# Nature of Component 
# 1 
# Mid semester Test 
# 90 mins. 
# 30
# 12/03 - 2.00 - 3.30PM
# Open Book 
# 2 
# Quizzes *
# 50 mins.
# 20 


# Closed book
# 3
# Classroom participation


# 10


# Open book
# 4
# Comprehensive Examination 
# 3 hours. 
# 40
# 08/05 AN
# Closed Book 









# General Chemistry(CHEM F111):-
# Textbooks:-
# (i) Solomons's Organic Chemistry Global Edition
# IC:-Amit Nag
# IC Room Number :- B103
# IC Email:- amitnag@hyderabad.bits-pilani.ac.in
# IC Phone:- 040-66303-605
# Room Number:-F102
# MidSem Exam:-14/03 - 11.00 - 12.30PM
# Compre Exam:-13/05 AN
# Course Plan:-

# Lec. No.
# Learning Objectives
# Topics to be Covered
# Learning Outcomes of the Lectures
# Chapter in the Text Book
# 1-3
# Quantum Theory
# Origin of quantum mechanics; Black body radiation, Wavefunction, Uncertainty principle, Schrodinger equation - Simple Applications
# Relate the need for quantum theory. Define and consolidate new concepts to be used in quantum mechanics. Apply quantization of states and zero-point energy in simple systems.
# T1 12.1-12.7, 12.9
# (7A, 7B, 7C, 7E)
# 4-8
# Atomic Structure and Spectra
# Hydrogenic Atoms: Energy levels and Wavefunctions, Orbitals, spectral transitions, many-electron atoms: orbital approximation, Pauli principle, Aufbau principle, term symbols, (simple systems only), selection rule
# Identify the atomic orbital picture of H-atom from quantum mechanics; spin orbit coupling and atomic term symbols. Identify spin as another coordinate.
# T1 13.1-13.11, 13.17-  
# 13.19.
# (8A, 8B, 8D)
# 13.15-13.16 (8C) 
# 9-12
# Chemical Bonding: Valence Bond and Molecular Orbital Theories
# VB Theory: electron pair bond, hybridization, resonance, MO theory: LCAO, bonding and antibonding orbitals, homonuclear and heteronuclear diatomic molecules. Lewis theory and VSEPR model (self-study)
# Demonstrate successful description of chemical bond; examine the application of molecular orbital theory to diatomic molecules. Recall Lewis theory and VSEPR model.
# T1 14.1-14.14
# (9A, 9B, 9C)
# 13
# Thermodynamics: the First Law, Internal Energy and Enthalpy
# Thermodynamic systems, state functions, thermal equilibrium and temperature, work, internal energy and heat transfer, heat capacity.
# Comprehend the concept of energy; compare reversible and irreversible processes (work done), classify and compare thermodynamic functions, influence of temperature and pressure on thermodynamic functions, illustrate bomb type calorimeter. 
# T1 2.1-2.9
# (2A, 2B, 2C, 2D)
# 14-15
# Thermodynamics: the Second Law, Entropy, Gibbs Energy
# Natural and reversible processes, entropy and second Law, Calculation of entropy changes, absolute entropies, Gibbs energy.  
# Demonstrate understanding of key concepts related to the second law of thermodynamics, including alternative statements of the second law. Discuss energy transfer in the context of thermodynamics, differentiate between the entropy of system, surroundings and universe, calculate the changes. Compare reversible and irreversible processes (heat); evaluate entropy changes accompanying expansion, heating, phase transition, define third law of thermodynamics, estimate the standard reaction entropy and statistical entropy, spontaneity of a process in a closed system - concept of Gibbs free energy
# T1 4.1-4.13
# (3A, 3B, 3C, 3D)
# 16
# Spontaneity and Equilibrium
# Applications of entropy and Gibbs free energy in chemical reactions
# Calculate the change in free energy for a chemical change from tabulated thermodynamic data; predict the spontaneity of a reaction, determine how temperature effects spontaneity of physical & chemical change based on ΔH and ΔS. Relate and apply concept of chemical equilibrium and response of chemical equilibria to temperature and pressure. 
# T1 5.1 – 5.3, 7.1-7.4
# (4A, 5A)
# 7.5-7.6, 7.8 (5B, 5C) (SS)
# 17
# (partial portion is S.S.)
# Chemical Kinetics: Experimental Methods, Reaction Rates, Temperature Dependence
# Rate laws, order, rate constants, Arrhenius equation; rate-determining step, reaction mechanisms; steady-state approximation.
# (except the steady-state approximation, remaining portions are self-study).
# Define the rate and order of reactions, write the general form of the rate law, practical determination of order and rate constants from the available concentration values of reactants/products as a function of time. Usage of "methods of initial rates", "isolation method", half- life" concepts. Effect of temperature on the rates of reaction. Using steady state approximation to derive rate law theoretically for a possible mechanism.
# T1 10.1-10.9, 
# T1 11.4-11.7
# (6A, 6B, 6C, 6D-1, 6F)
# 18-20
# Vibrational and Electronic Spectroscopy
# General features, vibrational energy levels and spectra; electronic spectra: Franck-Condon principle, types of transitions
# Relating the interaction between light and matter, apply knowledge of detailed understanding of vibrational and electronic spectra of small molecules, isotope shifts, detailed understanding of electronic states of atoms, molecules, Franck-Condon principle; predict the possible vibrational frequencies and electronic transitions
# T1 12.9, 19.6 – 19.8; 19.11; 
# 20.1 – 20.4
# (7E, 13A, 13C.1-13C.3,
#  13C.5, 13D)
# T3: 2.15 – 2.16
# 21-24
# Nuclear Magnetic Resonance Spectroscopy
# Principles, chemical shift, fine structure, applications (identification of organic compounds).
# Understand the basic principles and techniques of nuclear magnetic resonance spectroscopy; apply the knowledge gained for identification of organic molecules.
# T1 21.1 – 21.4
# (14A, 14B.1-14B.2)
# T2: 9.1-9.8
# 25-26
# Conformations
# Rotation around sigma bonds, conformational analysis of butane, cyclohexane, and substituted cyclohexanes.
# Classify structural and constitutional isomers, explain the terms torsional energy, torsional strain, angle strain.  Judge the stabilities, identify cis and trans relationship for the substituents on cyclohexanes, draw chair form of cyclohexane with unambiguous representation of axial and equatorial substituents, reason for the stability between the two isomers.
# T2: 4.8-4.9, 4.10 (SS), 4.11-4.14
# 27-28
# Stereochemistry
# Isomerism, chirality, origin of optical activity, stereochemistry of cyclic compounds, resolution.
# Define stereochemistry, outline different types of isomerism, differentiate between configurational and conformational isomers, enantiomers, chirality, specific rotation, optical activity, diastereomers, meso compounds and racemic mixtures, designate the R and S configurations, explain geometrical isomerism, optical resolution.
# T2: 5.1-5.13, 5.15-5.18, 7.2
# 29-30
# Substitution reactions
# Nucleophilic substitution reactions (both SN1 and SN2) of alkyl halides.
# List the types of substitution reactions (mechanism). Analyse the role of substrate, solvent and nucleophile. 
# T2: 6.2-6.13
# 31-32
# Elimination reactions
# Elimination reactions of alkyl halides; Hoffmann and Cope elimination.
# Outline the types of elimination reactions. Explain the difference between Hoffman vs Zeitsev product. Identify the importance of substrate, solvent and base. Examine difference between nucleophile and base; Hoffman and Cope elimination mechanism. Compare substitution and elimination reactions.
# T2: 6.15-6.19, 7.5-7.8, 20.12
# 33-34
# Electrocyclic reactions
# Introduction to pericyclic reactions with emphasis on electrocyclic reactions
# Identifying pericyclic reactions and various types of pericyclic reactions. Electrocyclic reaction types and conditions. Understanding the outcome of electrocyclic reactions by FMO approach.
# Lecture notes
# S.S.
# Introduction to coordination compounds
# Double salts and coordination compounds. Werner’s work; identification of structure by isomer counting. Effective atomic no. concept. (Self-study)
# Demonstrate comprehensive and well-founded knowledge of structure and bonding theories relevant to inorganic molecular compounds. Interpret Werner’ theory, coordination compound, ligand and valency, describe coordination compounds, deduct the effective atomic number.
# T3: p194-201 (S.S.)
# 35-36
# VB theory and Crystal field theory for octahedral complexes
# Explanation for the stability of complexes according to crystal field theory.
# Explain and measure the stabilities of complexes using the crystal field splitting theory.
# T3: p203-213
# 37-39
# Jahn-Teller distortions; square planar and tetrahedral complexes
# How do geometrical distortions stabilize the system? Stability in other geometries.
# Interpret Jahn-Teller distortion.  Formulate the crystal field theory to understand square planar and tetrahedral complexes.
# T3: p214-222
# 40
# Chelates & Isomerism
# Different types of ligands and stabilization due to entropy factors and electron delocalization in the rings.
# Distinguish various types of ligands and isomerism in co-ordination compounds.
# T3: p222-224, 307, 351-352, 389, 793, 807; p232-236


# 1. Scope and Objective of the Course: This course highlights the comprehensive study of electronic structure of atoms, molecules and chemical reaction via introducing quantum chemistry, spectroscopy, the study of interaction between the matter and electromagnetic radiation, thermodynamics, chemical equilibrium, and chemical kinetics as a part of general physical chemistry. It also provides a comprehensive survey of the concepts involved in the study of conformations, stereochemistry, functional groups, reaction mechanisms and coordination chemistry as a part of organic and inorganic chemistry. 
# Evaluation Scheme:
# Component
# Duration
# Weightage (%)
# Date and Time
# Nature of component
# Midsem
# 90 min
# 30
# 14/03 - 11.00 - 12.30PM
# Closed Book
# Class Tests#
# -
# 20
# To be announced
# Open Book
# Class Interaction** 
# -
# 10 
# Continuous 
# Open Book
# Comprehensive Examination
# 180 min
# 40
#                     13/05 AN
# Closed Book






# WORKSHOP PRACTICE(ME F112):-
# Textbooks:-
# (i) Parashar, B S N & R K Mittal Elements of Manufacturing Processes
# IC:-SUJITH R
# IC Room No: E-207
#  IC Email: sujith@hyderabad.bits-pilani.ac.in / sujithrmme@gmail.com
# IC Phone: 040-66303687    


# Room Number:-F105
# MidSem Exam:-16/03 - 9.30 - 11.00AM
# Compre Exam:-20/05 FN
# 1. Course description (as given in the Institute Bulletin):
# Engineering materials, casting, forming, machining, joining, powder metallurgy, additive manufacturing, plastic processing, various other manufacturing processes and related laboratory exercises.
# Scope and Objective of the Course:
# This course is required for all first-degree students at first year level. The course will provide an overview of the techniques and applications of basic manufacturing processes used for producing finished articles from raw materials. The course is practice-orientated and requires that basic skills in handling of tools, machines and machine tools used in different manufacturing processes are acquired through the hands-on experience. The practical knowledge is supplemented by the lectures to provide the knowledge and genesis of various manufacturing processes. The primary objective of this course is to learn how the physical artifacts we use are manufactured and gain technical knowledge and skills. Much of the knowledge in the course is conceptual and no great mathematics is involved. This knowledge will be useful in whatever discipline the students are going to specialize.

# Course plan:-


# Lec #
# Learning Objectives
# Topics to be covered
# Chapter in the Text Book
# 1-2
# Introduction, Engineering Materials,
# Role of measurements and Quality
# Basics, ethics and safety in workshop, Material properties, Mechanical properties, Common engineering materials, Metrology, Quality, Limits & fits, Examples.
# T1-1
# T1-2
# T1-3
# 3
# Production of parts by casting processes
# Casting processes, Pattern making. Moulding, Moulding sands.
# T1-11
# 4
# Casting processes
# Pattern allowances, Examples. Yield, Cooling rate, defects
# T1-11
# 5
# Metal cutting basics
# Metal cutting, Machine tools, Cutting tools, Tool material.
# T1-4
# 6
# Metal cutting basics
# Types of tools, Tool geometry, Chips, Tool life.
# T1-4
# 7
# Lathe machine tool
# Lathe machine tool, Turning and other operations.
# T1-5
# 8
# Metal cutting & Lathe operations
# Hole making & allied operations
# Operating conditions, MRR, Examples
# T1-5
# T1-6
# 9
# Production of flat surfaces
# Shaping & planning machines
# T1-7
# 10
# Production of complex surfaces
# Milling machine, Types of milling operations, Operating conditions, Milling operations, MRR, Examples.
# T1-8
# 11
# Producing fine surface finish,
# Grinding and fine finishing process
# Abrasives, Grinding, Grinding wheel, Grinding machines, fine finishing operations.
# T1-9
# 12
# Production of parts by forming processes, Sheet metal working
# Metal forming processes, Rolling, Extrusion, Forging, Punches and dies,  Sheet metal operations
# T1-12
# T1-13
# 13-14
# Powder metallurgy,
# Mechanical joining processes
# Metal powders: mixing, compaction, sintering, etc.
# Mechanical joining, Welding (arc, gas), Soldering, Brazing, Fasteners, Examples.
# T1-14
# T1-15
# 15
# Additive manufacturing and Plastics in manufacturing
# Processing of plastics, Types of plastics, Processing.
# T1-16


# Evaluation Schema:-

# EC No.
# Component
# Duration
# Weightage (%)
# Date & time
# Nature
# 1
# Mid Semester Exam
# 60 min
# 15
# 16/03 - 9.30 - 11.00AM
# CB
# 2
# Comprehensive exam
# 120 min
# 25
# 20/05 FN
# CB
# 3
# Classroom assessment


# 10


# --
# 4
# Laboratory Practical Regular classwork 


# 40 
# ---
# OB
# 5
# Laboratory Practical Comprehensive exam 


# 10 
# To be announced later
# OB






# CHEMISTRY LABORATORY(CHEM F110):-
# IC:-NILANJAN DEY
# IC Room No: B106
#  IC Email: nilanjan@hyderabad.bits-pilani.ac.in 
# IC Phone: 040-66303778
# Textbooks:-
# Lab Manual for Chemistry Laboratory
# Room Number:-B124
# MidSem Exam:-09/03 - 3.30 - 5.00PM
# Compre Exam:-04/05 FN

# PHYSICS LABORATORY(PHY F110):-
# IC:-Prasant Samantray


# Room Number:-A222
# Textbooks:-
# Lab manual for Physics
# MidSem Exam:-14/03 - 9.30 - 11.00AM
# Compre Exam:-15/05 AN












# Group 2

# COMPUTER PROGRAMMING(CS F111):-
# IC:- NIKUMANI CHOUDHURY
#  IC Email: nikumani@hyderabad.bits-pilani.ac.in
# IC Phone: +91 40 66303757
# Textbooks:- Hanley and Koffman Problem solving and program design in C Pearson, 2014
# Room Number:-F105 

# MidSem Exam:-15/03 - 2.00 - 3.30PM 
# Compre Exam:-17/05 FN


# Scope and Objectives of the Course: 
# This is an introductory course to computers and programming. The language used to explain the concepts is preferably C. This course uses a bottom-up approach to teach the beginners what is the structure of a computer and how it can be programmed. It also covers adequate knowledge of Number systems. The course starts with the process of creating or developing algorithms/ flowcharts for solving different types of problems using a Computer. At a later stage, it covers programming constructs used in most languages like C, C++, etc. including data types, variables, operators, input/output, decision making, loops, arrays, functions, structures, dynamic memory allocations, file handling. Students also get hands on experience C programs in the laboratory. 
# The primary objectives of the course are to introduce: 
# Basic representation of data and how to process this data using different types of storage representations inside a computer. 
# Algorithm development for different tasks to be executed on a Computer and programming these using the high-level languages.


# Course Plan:-

# Lecture#
# Learning Objectives
# Topics to be covered
# Chapter in the Text Book
# 1-2
# Introduction to Computers.
# Historical perspective to computing, Basic structure of a computer, H/w and S/w, Basic operations, Programming languages, Anatomy of a computer, Classification of Computers. 
# T1 (1)
# 3-4
# To understand how simple numeric data is represented inside a computer.
# Number systems, Data representation, Binary arithmetic, Conversion from one base to another, Complement representations of negative numbers. 
# Lecture notes
# 5-6
# To create algorithms for solving problems.
# Concept of an algorithm and its design, Flowcharts.
# R1 (1)
# 7-8
# Transition of an algorithm to a program, Concept of a program.
# R1 (2)
#      9-10
# To understand the concept of problem solving using digital computer as a concrete engineering activity.
# The use of programming language ‘C’ for problem solving.
# To understand specific constructs in C as tools available for handling specific class of problems.
# Representation and Manipulation of data (data types)
# T1(2)/
# R1(3)
# 11
# Evaluation of expressions (Operations on simple data)
# T1(2)/
# R1(4)
# 12-13
# Input and Output Operations including formatting. 
# T1(2)/
# R1(5)
# 14-15
# Sequential Evaluation and Conditional Evaluation
# (Sequential and conditional statements)
# T1(4)/
# R1(6)
# 16-18
# Iterative/Repetitive constructs
# T1(5)/
# R1(7)
# 19-20
# Programming using iterative/ repetitive constructs.
# T1(5)/
# R1(7)
# 21-23
# Arrays
# T1(7)/
# R1(8)
# 24-26
# Strings
# T1(8)/
# R1(9)
# 27-30
# Modular programming: User defined functions. 
# T1(3)/
# T1(10) 
# 31-33
# Pointers
# T1(6)/
# R1(12)
# 34-36
# Structures & Unions
# T1(10)/
# R1 (11)
# 37-38
# Dynamic memory allocation in C: malloc, calloc, realloc, free, linked lists etc.    
# T1(13)/
# R1 (14)
# 39-40
# File management in C.
# T1(11)/
# R1 (13)


# Evaluation Scheme:-

# Component
# Duration
# Weightage(%)
# Date & Time
# Nature of Component
# Mid-sem
# 90 mins
# 30%
# 15/03 - 2.00 - 3.30PM
# Closed Book
# Continuous Lab Quiz
# Lab Duration
# 10%
# In Lab (best 10/13)
# Open Book
# Class Interaction/Quiz
# In class
# 10%
# In class (best 10/15)
# Open Book
# Lab Exam
# 60 mins
# 10%
# TBA
# Open Book
# Comprehensive
# 180 mins
# 40%
# 17/05 FN
# Closed Book



# GENERAL BIOLOGY(BIO F111):-
# IC:-NAGA MOHAN K
# IC Email: mohankn@hyderabad.bits-pilani.ac.in
# IC Phone: 040-66303608

# Textbooks:- Simon, E.J. et. al. Campbell Essential Biology with Physiology
# (5th edition). Noida: Pearson India Education Services Pvt. Ltd., 2016
# Room Number:-F104
# MidSem Exam:-12/03 - 2.00 - 3.30PM 
# Compre Exam:-08/05 AN


# Course Description: This is an introductory/ foundation level course, where students are expected to learn about living systems and their properties, major biological compounds, basic biochemical and physiological processes. Students will also get introduced to genetics and recombinant DNA technology and their applications in daily life. While designing the course, care has been taken to relate the principles of biology with other science and engineering disciplines, wherever possible.
 
# Scope and Objective: Some students question the need for a course in biology, especially when their area of study is not related to biology (or science). However, it is becoming increasingly important to understand the nature of science and fundamental biological concepts for any person, regardless of his or her occupation. In this context, through this course it has been intended to impart knowledge on biological system with respect to nature, behavior and functioning of the cell. Further, this course has also been designed to make the student understand intricate relationship that living organisms have with their environment, at the molecular level, so that impact of modern biological research can be understood and appreciated by them. It is expected that at the end of this course, students would become aware of the influence of biology in almost every aspect of their lives.
 
# Intended Learning Outcomes: After successful completion of this course, students will be able to but not limited to:
 
# ❖ Comprehend various aspects of biology
# ❖ Understand biomolecules, and enzymes
# ❖ Outline cell structure and function
# ❖ Appreciate biochemical pathways
# ❖ Explain molecular basis of heredity and genetic diversity
# ❖ Apply biotechnology to some aspects of daily life
# ❖ Compare and contrast material exchanges in human body
# ❖ Examine human body’s control mechanism including reproduction

# Course Plan:-
# ​​

# Lecture
# No.
# Learning
# Objectives
# Topics to be covered
# Chapter 
# No.
# 1
# (10-01-2024)
# Getting introduced to the course
# Orientation to the course content; the scientific method; properties of life, Science and Theories in Science and Classification
# TB:1
# RB1: 1
# Class Notes
# 2-4
# (11-01-2024 –  (17-01-2024)
# Organic chemistry of living things and nutrition
# Building blocks; proteins; carbohydrates; lipids; nucleic acids;
# TB:3, 5
# RB1: 3, 5
# Class Notes
# 5-7
# (18-01-2024 – 24-01-2024)
# Cell Structure and Function
# Cell theory; prokaryotic and eukaryotic cells; brief overview
# of cellular organelles; membrane transport mechanisms
# TB:4
# RB: 4
# Class Notes
# 8-11
# (30-01-2024 – 07-02-2024)
# Bioenergetics; Respiration:
# Harnessing biochemical energy
# ATP; enzymes; Basic concepts of nutrition
# Biochemical Pathways - Cellular respiration: three stages of generating ATPs; process of fermentation
# TB:6
# RB: 6
# Class Notes
# 12-13
# (13-02-2024 – 14-02-2024)
# Bioenergetics; Photosynthesis:
# Obtaining energy from sunlight and conversion to biochemical energy
# Biochemical Pathways - Photosynthesis: light reactions, Calvin cycle; autotrophs and heterotrophs
# TB:7
# RB: 7
# Class Notes
# 14-16
# 15-02-2024 – 21-02-2024)
# Cellular functions at Molecular level (DNA as genetic material and expression of genes)
# DNA structure and its discovery, DNA replication; the genetic code; transcription; eukaryotic RNA processing; translation; mutations; viruses
# TB:10
# RB: 8
# Class Notes
# 17
# (22-02-2024)
# Controlling the cellular functions (Genetic regulation)
# How and why genes are controlled?
# TB:11
# RB: 11.3 - 11.5
# Class Notes
# 18
# (27-02-2024)
# The process of cloning organisms
# Cloning plants and animals; stem cells
# TB:11
# RB: 11.3 - 11.5
# Class Notes
# 19-20
# (28-02-2024 – 29-02-2024)
# Biotechnology and its Applications
# Techniques of DNA manipulation; GMOs; DNA Fingerprinting; bioinformatics; forensic science; biotechnology ethics
# TB:12
# RB: 11.1 – 11.2
# 21-24
# (05-03-2024 – 19-03-2024)
# Cell Division - Proliferation and Reproduction
# Cell cycle and Mitosis; stages of mitosis; cancer and cell cycle; Meiosis - stages and generation of genetic diversity; chromosomal abnormalities; the genetic basis of cancer
# TB:8,11
# RB: 9
# Class Notes
# 25-27
# (20-03-2024 – 26-03-2024)
# Patterns of Inheritance
# Mendelian genetics - laws of heredity; extensions to Mendel; other influences on phenotype
# TB:9
# RB1: 10
# Class Notes
# 28-29
# (27-03-2024 – 28-03-2024)
# Genetic diversity within species
# Speciation; Gene pool concept; Hardy-Weinberg equilibrium and its applications 
# RB1: 12.1-12.4, 13.1-13.5, 13.9
# Class Notes
# 30-33
# (02-04-2024 – 16-04-2024)
# Unifying Concepts of Animal Structure and
# Function
# Regulating internal body environment; Human circulatory, respiratory, digestive (including nutritional requirements) and excretory systems
# TB: 13,14,15
# RB1: 24, 25
# Class Notes
# 34-35
# (18-04-2024 – 23-04-2024)
# Nervous System
# Organization of the nervous system; nerve signal transmission; central and peripheral nervous systems
# TB:19
# RB1: 26.1-26.2
# Class Notes
# 36-37
# (24-04-2024 – 25-04-2024)
# Body’s defense strategies
# Innate immunity; lymphatic system; adaptive immunity
# TB:16
# RB1: 26.7
# Class Notes
# 38
# (30-04-2024)
# Hormonal system
# Different hormones, their production sites, and modes of action
# TB:17
# RB1: 26.3
# 39-40
# (01-05-2024 – 02-05-2024)
# Human reproduction and embryonic development
# Human Reproduction, Sex and Sexuality - gametogenesis; male and female reproductive systems – hormonal controls;
# pregnancy and early human development
# TB:18
# RB1: 27
# Class Notes


# Evaluation Scheme:-

# Evaluation component
# Duration
# Weightage % (Marks)
# Date and Time
# Nature of the Component
# Mid-Semester Examination
# 1.5 hours
# 25% (75M)
# 12-03-2024
# (2:00-3:30 PM)
# Closed Book
# Announced Quizzes 
# (Best 3 out of 4)
# 30 min
# 30% (90 M)
# TBA
# Closed Book, MCQ-based questions
# Comprehensive Examination
# 3 hours
# 35% (105 M)
# 08-05-2024
# (AN)
# Closed Book (15%) + 
# Open Book (20%)
# End of the class evaluation
# Variable
# 10% (30 M)
# Continuous
# MCQ-based questions, closed book*




# THERMODYNAMICS(BITS F111)
# IC:- SRIKANTA DINDA
# IC Email:  srikantadinda@hyderabad.bits-pilani.ac.in 
# IC Phone: 040-66303586

# Textbooks:- Borgnakke Sonntag Fundamentals of Thermodynamics 10th Edition, Wiley India Adaptation
# Room Number:-F105
# MidSem Exam:-14/03 - 11.00 - 12.30PM
# Compre Exam:-13/05 AN
# Course Description:
# Basic concepts and laws of thermodynamics; macroscopic thermodynamic properties; application to thermodynamic systems (closed and open); microscopic approach to estimate the entropy of a system; equation of state; efficiency, irreversibility, and availability of thermodynamic systems.
# Scope and Objective:
# Thermodynamics deals with the matter, energy, and the laws governing their interactions in a given system. Therefore, it is essential to learn its importance in the design and analysis of processes, devices, and systems for effective utilization of energy as well as matter. The course emphasizes the fundamental concepts and the laws of thermodynamics applied to closed systems (control mass) and open systems (control volume). Irreversibility and availability are the powerful tools used in the design and analysis of systems and therefore will be discussed in detail.
# Expected Learning Outcome:
# Understand the fundamentals of thermodynamic systems - processes and cycles
# Solve problems related to pure substances using thermodynamic tables 
# Apply the first-law to systems involving heat and work interactions
# Understand the second-law and its applications - closed and open systems
# Solve problems using the first and second laws of thermodynamics
# Understand the basic concepts and principles of the second-law - entropy, irreversibility, and availability




# Course Plan:-

# Lecture No.
# Learning objectives
# Topics to be covered
# Chapter & Sections in TB
# 1 ‒ 3
# Understand the basic concepts and definitions pertaining to thermodynamics (TD) 
# Introduction, thermodynamic systems, state properties, process & cycle, specific volume, zeroth-law, temperature scales, applications 
# 1.1 ‒ 1.12
# 4 ‒ 5
# Understand the properties of pure substances (as working media)
# Pure substance, states, phase equilibrium, independent properties, equation of state, compressibility factor
# 2.1 – 2.3, 
# 2.5 – 2.10
# 6 ‒ 7
# Use of thermodynamic tables to predict the properties of pure substances
# Thermodynamic properties and tables of standard substances (as working fluids)
# 2.4
# 8 ‒ 11
# Understand the concepts of boundary work and heat transfer and solve problems of control-mass (CM) as a system
# Definition of work and heat and their notation, work done at system’s boundary, modes of heat transfer
# 3.1 – 3.6
# 12 ‒ 15
# Understand the first-law of TD for a CM, and other forms of energy involved
# First-law for a process; internal energy and enthalpy; specific heats of ideal gases
# 3.7– 3.11
# 16 ‒ 18
# Apply the first-law of TD to solve problems of CM as a system
# First-law as a rate equation; problem analysis and solution technique; examples of closed systems
# 3.13 – 3.15
# 19 ‒ 21
# Difference between control-mass (CM) and control-volume (CV). Understand the first-law of TD for a CV
# Conservation of mass in a control-volume (CV); first-law for a CV; steady-state and transient processes
# 4.1 – 4.4, 4.6
# 22 ‒ 23
# Application of the first-law of TD for a CV
# First-law as a rate equation; problem solving techniques; examples of CVs
# 4.7
# 24 ‒ 27
# Understand the need for Second-law of TD and its basic concepts
# Limitations of the first-law and need of the second-law; reversible process; heat engine, heat pump, refrigerator; Carnot cycle; COP, Kelvin-Planck & Clausius statements; Carnot cycle; thermodynamic temperature scale
# 5.1 – 5.11
# 28 ‒ 32
# Understand the principles of entropy and second-law of TD for a CM
# Concept of entropy; the need and definition of entropy; entropy of a pure substance; entropy change of a reversible and irreversible processes; principle of increase of entropy, thermodynamic property relation; problem solving
# 6.1 – 6.11
# 33 ‒ 36
# Understand the formulation of second-law of TD for a CM (as a system)
# Second-law for a control-volume (CV); steady-state and transient processes; reversible process; principle of increase of entropy
# 7.1 – 7.5
# 37 ‒ 39
# Application of second-law of TD for a CV
# Understanding the efficiency and performance of systems; problem solving
# 7.5
# 40 ‒ 42
# Understand the principles of Irreversibility and availability
# Available energy, reversible work and irreversibility; second-law efficiency
# 8.1 – 8.4



# Evaluation Scheme:-

# Evaluation Component
# Duration (min.)
# Weightage (%)
# Date & Time
# Nature of Component
# Midsem Test*
# 90
# 30
# 14/03 - 11.00 - 12.30PM
# Closed Book
# Tutorial Tests
# 20
# 20
# In tutorial classes
# Open Book
# Quizzes
# 15
# 10
# In lecture/ tutorial classes
# Open Book
# Comprehensive Exam*
# 180
# 40
# 13/05 AN
# Closed Book





# BIOLOGY LABORATORY(BIO F110)
# IC:-Sridev Mohapatra
# IC Email:  sridev.mohapatra@hyderabad.bits-pilani.ac.in
# IC Phone: 406-630-3604

# Textbooks:- Same as Part iv: Biology Faculty MT-I Biology, Notes EDD, 2007 Lab Manual for Biology Laboratory Notes EDD, 2012
# Room Number:-A122 
# MidSem Exam:-09/03 - 3.30 - 5.00PM 
# Compre Exam:-04/05 FN

# TECHNICAL REPORT WRITING(BITS F112)
# IC:-PRANESH BHARGAVA 
# IC Email: pranesh@hyderabad.bits-pilani.ac.in
# IC Phone:+91 40 66303524
# Textbooks:- Hewings, M. and Thaine C Cambridge Academic English (Advanced) Student’s Book First South Asian Edition. Cambridge University Press
# Room Number:-F103
# MidSem Exam:-13/03 - 4.00 - 5.30PM 
# Compre Exam:-15/05 AN
# Scope and Objective of the Course:
# The main objective of the course is to help the learners develop skills in writing technical reports and making academic presentations. The focused skill areas are meant to enable students to write their PS, LoP/DoP reports and theses.


# Course Plan:-

# LectureNo.
# Learning objectives
# Topics to be covered
# Chapter intheTextbook
# 1
# Understand the nature and purpose ofthe
# course
# Course overview: importance; objective;topics; assessment.


# 2
# Discover differentaspects of technicalcommunication
# Overview of technical communication:writing in the technical workplace;attributes of technical writing; the writing
# process; the means to master technicalwriting.
# RB1: Ch. 1.
# 3–8
# Acquire effectivegrasp of elements oftechnical writing
# Elements of effective writing: technicalsentences; technical paragraphs;parallelism, lists, and layout; routinecorrespondence
# RB1: Ch. 2–
# 5; 
# 9-12
# Acquire effectivegrasp of elements oftechnical writing
# Overview of punctuation and grammar;
# mechanics and conventions; ethics.
# RB1: Appendix A,B, C.
# 13-18
# Acquire effectivegrasp of elements oftechnical writing
# Technical definitions and descriptions; instructions, procedures, and manuals
# RB1: Ch.12;
# Ch. 13
# 19–20
# Become competent to practice-draft parts of various reports
# Types of reports: documents that report on past events or completed tasks; documents that report on ongoing tasks (progress reports); documents that recommend future actions; documentsthat define
# standards (specifications); lab reports.
# RB1: Ch. 6.
# 21–23
# Acquire the ability to practice-draft partsof
# a formal report;
# Learn the process ofwriting and revisingparts of a formal
# Report;
# Understand thesources of your data
# Formal reports: parts of a formal report;formal report pagination; references and
# Citations;
# Preparatory steps for writing reports:planning your document; drafting andrevising your document;
# Methods and sources of data:
# interviewing; surveying; observing andtesting; published information.
# RB1: Ch. 7;
# Ch. 9.
# 24–25
# Learn to useillustrations
# Use of illustrations: putting graphics intoreports; rules for incorporating reportgraphics; avoiding graphical
# misrepresentation.
# RB1: Ch.10.
# 25-28
# Recapitulate and revise the concepts while practising
# Revision, Recap and Writing practice
# RB1: All chapters



# Evaluation Scheme:-

# Component
# Duration
# Weighting(%)
# Date & Time
# Nature ofComponent
# Mid-semesterTest
# 90 Minutes
# 30
# As announced in thetimetable
# CB
# Assignments
# To be announced
# 30
# To be announced
# OB
# Class participation
# Varying
# 10
# Distributed throughout the semester
# OB / CB
# Comprehensive
# Examination
# 3 Hours
# 30
# As announced inthe
# timetable
# CB




# ENGINEERING GRAPHICS(BITS F110)
# IC:-A Vasan
# IC Room no.:-D-117
# IC Email: vasan@hyderabad.bits-pilani.ac.in
# IC Phone:040-66303510

# Textbooks:- Kulkarni D M and Others Engineering Graphics with AutoCADPHI,2009
# Room Number:-F102
# MidSem Exam:-16/03 - 9.30 - 11.00AM 
# Compre Exam:-20/05 FN
# 1. Course Description
# Introduction to AutoCAD commands, simple drawings, orthographic projections, projections of points, lines, planes; auxiliary projections; projections and sections of solids; development of surfaces; isometric projections.
# 2. Scope and objective of the course:
# Engineering Graphics is the primary medium for development and communicating design concepts. Through this course, the students are trained in Engineering Graphics concepts with the use of AutoCAD. The latest ISI code of practice is followed. Computerized drawing is an upcoming technology that provides accurate and easily modifiable graphics entities, easy data storage and retrieval facility, and enhances creativity. 


# Course Plan:-

# Lecture No.
# Learning Objectives
# Topics to be covered
# Practical
# Classes
# Chapter in the Text Book
# 1
# Introduction to EG
# Basic concepts and Handout discussions
# -
#           1
# 2-3
# Introduction to  
# AutoCAD
# Basic commands 
# 3
# 1 & 2
# 4-5
# Orthographic projections
# Theory, techniques, first and third angle projections, 
# Multi view drawing from pictorial views. 
# 2
# 3 & 5
# 6-7
# Projections of Points and Lines
# Positions, notation system, and projections procedure, Positions, terms used, different cases, traces of a line and projections procedure  
# 2
# 9
# 8
# Projections of Lines
# Positions, terms used, different cases, traces of a line and projections procedure  
# 1
# 10
# 9-10
# Projections of Solids and Sections of Solids
# Construction of right, regular, oblique solids; section planes and sectional view. 
# 2
# 12 & 13
# 11
# Development of surfaces
# Radial line, parallel line; anti-development 
# 1
# 14
# 12-13
# Isometric Projection
# Theory of isometric drawing, construction of isometric projection from orthographic. 
# 2
# 6


# Evaluation Scheme:-

# EC No.
# Evaluation component
# Duration
# Weightage (%)
# Date, Time 
# Nature of Component
# 1
# Mid sem test (CBT)
# 60 min
# 20
# 16/03 - 9.30 - 11.00AM
# Closed Book
# 2
# Comprehensive Test (CBT)
# 90 min
# 30
# 20/05 FN
# Closed Book
# 3
# Practical (CAD Software)
# -
# 30
# Once a week
# Open Book
# 4
# Tutorial
# -
# 20
# Once a week
# Open Book




# MATH 

# MATHEMATICS II(MATH F112)
# IC:-Deepika 
# IC Email: deepika@hyderabad.bits-pilani.ac.in
# IC Phone+91 40 66303589

# Textbooks:- Churchill, R V and James W, Complex Variables and Applications 8th Edition, 2008, McGraw-Hill
# Room Number:-F108
# MidSem Exam:-11/03 - 11.00 - 12.30PM 
# Compre Exam:-06/05 AN
# Scope and Objective of the Course: The course is made for Pharmacy students keeping in mind the importance of Calculus and differential equations in every branch of Science and Engineering. Functions of several variables appear more frequently in Science than functions of a single variable. Their derivatives are more interesting because of the different ways in which the variables can interact, while differential equations of both homogeneous and non-homogeneous also plays a vital role in Engineering and Sciences. This course includes Polar Co-ordinates, Functions of several variables, Multiple Integrals, Vector Valued functions, Complex functions and Ordinary differential equations.
# Course Plan:-

# Lect. No.
# Broad Topic
# Learning objectives
# Sub-topics to be covered
# Article




# Topic I
# 1-2
# Polar co-ordinates
# How to obtain length of a polar curve and area of a surface of revolution of a polar curve?
# Introduction to PC- Relation between Cartesian and polar, Polar curves
# 11.3-11.5
# 3-10
# Function of several variables
# Mathematical definition of a local Maximum and Minimum.  Use of chain rule. 
# Limit, Continuity,Partial derivatives,Chain rule, Directional Derivative, Extreme values and Saddle point, Lagrange Multipliers
# 14.1-14.5
# 14.7-14.8
# 11-15
# Multiple Integrals
# How formula for area in polar coordinates can be found through polar double integral?
# Double integral, Double integral in polar form
# 15.1-15.4
# 16-17
# Vector valued functions
# Appreciate the concepts of vectorial representation 
# Vector valued functions and Space curves
# 13.1




# Topic II
# 18-22
# Complex functions and their analyticity
# Mathematical definitions of complex valued functions 
# Complex number, root and functions, Derivative and CR equations and Analyticity
# 13.1-13.4




# Topic III
# 23-27
# First order ODES
# Learning to develop basic mathematical modelling
# Introduction (Degrees and Order), Linear first order ODE, Linear differential equations, Separable and Exact ODE
# 1.1-1.4
# 28-34
# Second order ODES
# Learning to develop higher level of  mathematical modelling
# Second order linear homogenous ODE, Cauchy-Euler ODE, NON-homogenous ODE
# 2.1-2.3, 2.5, 2.7
# 35-40
# Laplace transformations
# A different tool to solve the mathematical models.
# Laplace transformations, Solutions of ODE using Laplace transformations
# 6.1-6.7

# Evaluation Scheme:

# Sl. No.
# Evaluation Component
# Duration
# Weightage
# (%)
# Date and Time
# Nature of Component
# 1
# Quiz
# TBA
# 15
# TBA
# Open book
# 2
# Mid-semester Exam
# 90 minutes
# 25
# 11/03-11-12:30 
# Closed book
# 3
# Assignment
# TBA
# 15
# TBA
# Open book
# 4
# Comprehensive Exam
# 180 minutes
# 45
# 06.05.2024 (AN)
# Closed book




# PROBABILITY AND STATISTICS(MATH F113) 
# IC:-Sayan Ghosh
# IC Room no.:- H024
# IC Email: sayan@hyderabad.bits-pilani.ac.in
# IC Phone: 040-66303642 
# Textbooks:- Jay L Devore Probability and Statistics for Engineering and the Sciences 8th Edition,
# Cengage Learning, 2012
# Room Number:-F102 
# MidSem Exam:-13/03 - 9.30 - 11.00AM 
# Compre Exam:-10/05 AN
# 1.   Scope and objective of the course:
# Probability theory deals with many real-life problems, which either inherently involve the chance phenomena or describing the behaviour of the system explicitly with statistical properties. Interpretation of the system behaviour in many engineering and sciences depends on concept of probability and statistics that familiarize with the computational and analytical aspects. The course deals with the basic properties of various distributions and other related things.

# Lecture Plan:
# ​​
# Lecture
# Learning Objectives
# Topics to be covered
# Chapter in the Text Book
# 1-3
# Probability theory makes predictions about experiments whose outcomes depend upon chance.  
# How to state the three axioms of probability and use them to derive basic facts about a probability function. Learn about three approaches of defining probabilities and their interpretations. Introduce conditional Probability and its applications
# Quick Review of the following Concepts
# Introduction to probability, sample spaces and events, Axioms, Interpretations and Properties of Probability, Conditional Probability, Independence.
# 2.1-2.5
# 4-5
# To gain knowledge on how to define a random variable and identify various important and commonly used discrete distributions.
# Random Variables, Probability Distributions for Discrete Random Variables, Expected Values, Moment Generating Function (MGF)
# 3.1, 3.2, 3.3,
#  5.11 (R-1)
# 6-9
# The Binomial Probability Distribution, Hypergeometric and Negative Binomial Distributions, Geometric Distribution, The Poisson Probability Distribution
# 3.4, 3.5, 3.6
# 10-12
# To gain knowledge on various important and commonly used continuous distributions
# Continuous Random Variables, Probability Density Functions, Cumulative Distribution Functions and Expected Values, Moment Generating Function (MGF)
# 4.1, 4.2,
# 5.11(R-1)
# 13-17
# To gain knowledge on most important continuous distribution (Normal distribution) and its applications in real life.
# The Normal Distribution, The Exponential and Gamma Distributions, Chi-Square, Log Normal Distributions and Transformation Methods to Obtain Distributions.
# 4.3, 4.4, 4.5,
# 6.7 (R-1)
# 18-19
# Introduce simulation and how to simulate complex systems.
# Simulation – Discrete and Continuous random variables
# 4.10 (R-1),
# 5.14 (R-1)
# 20-22
# Develop probability models involve several random variables simultaneously
# Jointly Distributed Random Variables, Expected Values, Covariance, and Correlation
# 5.1, 5.2
# 23-25
# Introduce Statistics and their distributions.
# Statistics and Their Distributions, The Distribution of the Sample Mean, The Distribution of a Linear Combination
# 5.3, 5.4, 5.5
# 26-27
# How to estimate population’s parameters.
# Some General Concepts of Point Estimation, Methods of Point Estimation
# 6.1, 6.2
# 28-31
# Basic Properties of Confidence Intervals, Large-Sample Confidence Intervals for a Population Mean and Proportion, Intervals Based on a Normal Population Distribution, Confidence Intervals for the Variance and Standard Deviation of a Normal Population
# 7.1, 7.2, 7.3, 7.4
# 32-34
# Introduce concepts of hypothesis testing and its applications in real world problems
# Hypotheses, Test Procedures and P-values, z-tests for hypothesis about a Population Mean
# 8.1, 8.2
# 35-37
# One sample t-test, Tests Concerning a Population Proportion
# 8.3, 8.4
# 38-40
# Objective is how to exploit the relationship between two or more variables   by introducing predictive models.
# The Simple Linear Regression Model, Estimating Model Parameters, Correlation
# 12.1,12.2,12.5


# Evaluation Scheme:

# Evaluation Component
# Duration
# Weightage
# Date & Time 
#  Nature of Component
# Classroom Participation


# 10%




# Quiz- 1
# To be announced in the class
# 10%
# To be announced in the class
# Closed Book
# Mid Semester Examination
# 90 mins
# 30%
# 13/03 - 9.30 - 11.00AM
# Open book
# Quiz- 2
# To be announced in the class
# 10%
# To be announced in the class
# Closed Book
# Comprehensive Examination
# 180 mins
# 40%
# 10/05 AN
# Closed Book



# MATHEMATICS I(MATH F111 )
# IC:-B MISHRA
# IC Room no.:- H025
# IC Email: bivu@hyderabad.bits-pilani.ac.in
# IC Phone:+91 40 66303532
# Textbooks:- George B. Thomas, Maurice D. Weir and Joel Hass, Thomas Calculus Pearson, 14th Edition, 2018
# Room Number:-F104 
# MidSem Exam:-09/10 - 2.00 - 3.30PM 
# Compre Exam:-07/12 FN
# 2. Scope and Objective of the Course:  Calculus is fundamental to every branch of science and engineering, as all dynamics is modeled through differential and integral equations.  Functions of several variables appear frequently in science.  The derivatives of the functions of several variables are more interesting because of the several degrees of freedom available.  The integrals of the functions of several variables occur in several places such as probability, fluid dynamics, electrical sciences, just to name a few. All lead in a natural way to functions of several variables.  The objective of the course is to lay the foundations for these topics.
# Course Plan:
# Module Number: Limits and continuity of real valued function of one real variable
# Lecture session/Tutorial Session:
# Self Study: Properties of limits, infinity as a limit, continuity
# Ref. to text Book: chap/Sec. 2.3 to 2.6
# Learning Outcome: Understanding of real valued functions of one real variable
# Module Number: Infinite sequences and series
# Lecture session/Tutorial Session:
# L1: Convergence of sequences and series of real numbers
# L2-L3: Different tests of convergence for the series of non negative terms
# L4: Absolute and conditional convergence, alternating series
# Ref. to text Book: chap/Sec. 10.1 - 10.8 10.1 is for self study
# Learning Outcome: Differentiate clearly between three types of series convergence with examples and counter examples, Approximating functions with polynomials
# Module Number: Polar coordinates
# Lecture session/Tutorial Session:
# L5: Power series, Maclaurin series, Taylor series of functions
# L6: Polar coordinates
# L7-L8: Graphing in polar coordinates
# L9: Integration using polar coordinates.
# L10: Polar equations of conic sections
# Ref. to text Book: chap/Sec. 11.3 - 11.5, 11.7
# Learning Outcome: The curvilinear coordinate systems like polar coordinates can be more natural than Cartesian coordinates many a times








    """


    #user_input= "is there a clash in the compres of thermodynamics and computer programmming"

    prompt = ChatPromptTemplate.from_template(
            f"""Answer the question in 100 words {user_input}  after going through the context {course_details} """
        )
    chain= LLMChain(llm=llm, prompt=prompt)

    result = chain.run(user_input=user_input)

    print(result)
    return result

